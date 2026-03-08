from django.urls import path
from .views import landing_page, blog_detail_page

app_name = "landing"

urlpatterns = [
    path("", landing_page, name="home"),
    path("blog/<int:pk>/", blog_detail_page, name="blog-detail-page"),
]
