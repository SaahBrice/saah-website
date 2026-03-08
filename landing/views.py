from django.shortcuts import render, get_object_or_404
from blog.models import Blog
from blog.og_metadata import get_og_metadata


def landing_page(request):
    """Render the SAAH landing / coming-soon page with latest blog posts."""
    blogs = Blog.objects.all()[:6]
    og = get_og_metadata(
        request,
        title="SAAH — Coming Soon",
        description="A space built for serious students and workers. Coming to Buea.",
    )
    return render(request, "landing/index.html", {"og": og, "blogs": blogs})


def blog_detail_page(request, pk):
    """Render a single blog post with OG metadata for social sharing."""
    blog = get_object_or_404(Blog, pk=pk)
    og = get_og_metadata(
        request,
        title=blog.title,
        description=blog.subtitle or blog.title,
        image_url=blog.proxied_thumbnail_url,
        og_type="article",
    )
    return render(request, "blog/detail.html", {"blog": blog, "og": og})
