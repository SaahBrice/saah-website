# SAAH Blog API Documentation

> **Base URL:** `http://127.0.0.1:8000`
> 
> **Interactive Docs:** [Swagger UI](/api/docs/) • [ReDoc](/api/redoc/)

---

## Endpoints

### 1. List Blog Posts

```
GET /api/blogs/
```

Returns a paginated list of all blog posts (12 per page).

**Response** `200 OK`
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Welcome to SAAH",
      "subtitle": "Our first post",
      "proxied_thumbnail_url": "/proxy/media/?url=https://drive.google.com/...",
      "total_likes": 542,
      "publish_date": "2026-03-08T12:00:00+01:00",
      "edit_date": "2026-03-08T12:00:00+01:00"
    }
  ]
}
```

---

### 2. Blog Post Detail

```
GET /api/blogs/{id}/
```

Returns a single blog post with full content, media, and OG metadata.

**Response** `200 OK`
```json
{
  "id": 1,
  "title": "Welcome to SAAH",
  "subtitle": "Our first post",
  "content": "<p>Rich HTML content from TinyMCE...</p>",
  "proxied_thumbnail_url": "/proxy/media/?url=...",
  "proxied_audio_url": "/proxy/media/?url=...",
  "total_likes": 542,
  "real_likes": 42,
  "publish_date": "2026-03-08T12:00:00+01:00",
  "edit_date": "2026-03-08T12:00:00+01:00",
  "og_title": "Welcome to SAAH",
  "og_description": "Our first post",
  "og_image": "http://127.0.0.1:8000/proxy/media/?url=..."
}
```

---

### 3. Like a Blog Post

```
POST /api/blogs/{id}/like/
```

Increments the real like counter by 1. No authentication required.

**Response** `200 OK`
```json
{
  "real_likes": 43,
  "total_likes": 543
}
```

**Error** `404 Not Found`
```json
{
  "detail": "Blog post not found."
}
```

---

### 4. Media Proxy

```
GET /proxy/media/?url={original_url}
```

Proxies external media (images, audio) from Google Drive or other sources to avoid CORS and hotlink issues.

**Supported URL formats (Google Drive):**
- `https://drive.google.com/file/d/{FILE_ID}/view?usp=sharing`
- `https://drive.google.com/open?id={FILE_ID}`
- Any direct URL that is not a Drive link is also proxied

**Response:** Binary media with correct `Content-Type` header. Cached for 24 hours.

---

## Notes

- **Pagination:** All list endpoints use page number pagination (12 items/page). Use `?page=2` for subsequent pages.
- **Likes:** `total_likes` = `random_likes` (100–1000, auto-generated) + `real_likes` (user-driven).
- **Rich text:** The `content` field contains sanitized HTML from TinyMCE. Render it with `innerHTML` or `v-html`.
- **OG metadata:** The detail endpoint includes `og_title`, `og_description`, and `og_image` (absolute URL) ready for `<meta>` tags.
- **OpenAPI Schema:** Available at `GET /api/schema/` (JSON format).
