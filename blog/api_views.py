from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiResponse

from .models import Blog
from .serializers import BlogListSerializer, BlogDetailSerializer


class BlogListAPIView(generics.ListAPIView):
    """List all published blog posts (paginated)."""
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer

    @extend_schema(
        summary="List blog posts",
        description="Returns a paginated list of all blog posts ordered by publish date.",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BlogDetailAPIView(generics.RetrieveAPIView):
    """Retrieve a single blog post with full content and OG metadata."""
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer

    @extend_schema(
        summary="Get blog post detail",
        description="Returns a single blog post with full content, media, OG metadata, and like counts.",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BlogLikeAPIView(APIView):
    """Increment the real_likes counter for a blog post."""

    @extend_schema(
        summary="Like a blog post",
        description="Increments the real like counter by 1 and returns the new total.",
        responses={
            200: OpenApiResponse(description="Like registered successfully."),
            404: OpenApiResponse(description="Blog post not found."),
        },
    )
    def post(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response(
                {"detail": "Blog post not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        blog.real_likes += 1
        blog.save(update_fields=["real_likes"])

        return Response({
            "real_likes": blog.real_likes,
            "total_likes": blog.total_likes,
        })
