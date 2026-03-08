def get_og_metadata(request, **kwargs):
    """
    Build a dict of Open Graph metadata for use in templates.

    Usage in views:
        context["og"] = get_og_metadata(
            request,
            title="My Post",
            description="Post description",
            image_url="/proxy/media/?url=...",
            og_type="article",
        )

    In templates:
        <meta property="og:title" content="{{ og.title }}">
    """
    from django.conf import settings

    site_url = getattr(settings, "SITE_URL", "http://127.0.0.1:8000")
    site_name = getattr(settings, "SITE_NAME", "SAAH")
    default_desc = getattr(settings, "SITE_DESCRIPTION", "")

    title = kwargs.get("title", site_name)
    description = kwargs.get("description", default_desc)
    image_url = kwargs.get("image_url", "")
    og_type = kwargs.get("og_type", "website")
    url = kwargs.get("url", request.build_absolute_uri())

    # Build absolute image URL
    if image_url and not image_url.startswith("http"):
        image_url = request.build_absolute_uri(image_url)

    return {
        "title": title,
        "description": description,
        "image": image_url,
        "type": og_type,
        "url": url,
        "site_name": site_name,
    }
