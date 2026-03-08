from django.urls import path
from .api_views import BlogListAPIView, BlogDetailAPIView, BlogLikeAPIView

app_name = "blog"

urlpatterns = [
    path("", BlogListAPIView.as_view(), name="blog-list"),
    path("<int:pk>/", BlogDetailAPIView.as_view(), name="blog-detail"),
    path("<int:pk>/like/", BlogLikeAPIView.as_view(), name="blog-like"),
]
