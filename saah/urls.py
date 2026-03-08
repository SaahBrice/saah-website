from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from blog.proxy import proxy_media

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # TinyMCE
    path("tinymce/", include("tinymce.urls")),

    # Landing page (root)
    path("", include("landing.urls")),

    # Blog API
    path("api/blogs/", include("blog.urls")),

    # Media proxy (images + audio from Google Drive etc.)
    path("proxy/media/", proxy_media, name="proxy-media"),

    # API documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
