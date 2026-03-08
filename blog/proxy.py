import re
import requests
from django.http import HttpResponse, HttpResponseBadRequest


def _extract_gdrive_file_id(url: str) -> str | None:
    """Extract a Google Drive file ID from various share URL formats."""
    patterns = [
        r"/file/d/([a-zA-Z0-9_-]+)",   # /file/d/<id>/view
        r"id=([a-zA-Z0-9_-]+)",         # ?id=<id>
        r"/open\?id=([a-zA-Z0-9_-]+)",  # /open?id=<id>
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def proxy_media(request):
    """
    Proxy an external media URL (image or audio) so the browser can display it
    without CORS / hotlink issues.

    Usage:  /proxy/media/?url=<original_url>

    If the URL is a Google Drive share link it is converted to a direct
    download URL automatically.
    """
    original_url = request.GET.get("url", "")
    if not original_url:
        return HttpResponseBadRequest("Missing 'url' query parameter.")

    # Convert Google Drive share links to direct download URLs
    file_id = _extract_gdrive_file_id(original_url)
    if file_id:
        fetch_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    else:
        fetch_url = original_url

    try:
        upstream = requests.get(fetch_url, stream=True, timeout=15, allow_redirects=True)
        upstream.raise_for_status()
    except requests.RequestException:
        return HttpResponseBadRequest("Could not fetch the requested media.")

    content_type = upstream.headers.get("Content-Type", "application/octet-stream")

    response = HttpResponse(upstream.content, content_type=content_type)
    response["Cache-Control"] = "public, max-age=86400"
    return response
