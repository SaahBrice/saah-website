from rest_framework import serializers
from .models import Blog


class BlogListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for blog list views."""
    total_likes = serializers.IntegerField(read_only=True)
    proxied_thumbnail_url = serializers.CharField(read_only=True)

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "subtitle",
            "proxied_thumbnail_url",
            "total_likes",
            "publish_date",
            "edit_date",
        ]


class BlogDetailSerializer(serializers.ModelSerializer):
    """Full serializer with content, audio, and OG metadata."""
    total_likes = serializers.IntegerField(read_only=True)
    proxied_thumbnail_url = serializers.CharField(read_only=True)
    proxied_audio_url = serializers.CharField(read_only=True)

    # OG metadata for social sharing
    og_title = serializers.SerializerMethodField()
    og_description = serializers.SerializerMethodField()
    og_image = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "subtitle",
            "content",
            "proxied_thumbnail_url",
            "proxied_audio_url",
            "total_likes",
            "real_likes",
            "publish_date",
            "edit_date",
            # OG fields
            "og_title",
            "og_description",
            "og_image",
        ]

    def og_title(self, obj):
        return obj.title

    def get_og_title(self, obj):
        return obj.title

    def get_og_description(self, obj):
        return obj.subtitle or obj.title

    def get_og_image(self, obj):
        request = self.context.get("request")
        if obj.proxied_thumbnail_url and request:
            return request.build_absolute_uri(obj.proxied_thumbnail_url)
        return ""
