import random
from django.db import models
from tinymce.models import HTMLField


class Blog(models.Model):
    """Blog post with rich text, media proxying, and like tracking."""

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=500, blank=True)
    content = HTMLField()

    # Media — stored as external URLs (e.g. Google Drive share links)
    thumbnail_url = models.URLField(
        max_length=500,
        blank=True,
        help_text="Paste a Google Drive share link or any direct image URL.",
    )
    audio_url = models.URLField(
        max_length=500,
        blank=True,
        help_text="Paste a Google Drive share link or any direct audio URL.",
    )

    # Likes
    random_likes = models.PositiveIntegerField(
        editable=False,
        default=0,
        help_text="Auto-generated random number (100–1000) on creation.",
    )
    real_likes = models.PositiveIntegerField(
        default=0,
        help_text="Incremented every time a user clicks the like button.",
    )

    # Dates — both editable in admin
    publish_date = models.DateTimeField()
    edit_date = models.DateTimeField()

    class Meta:
        ordering = ["-publish_date"]
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.random_likes = random.randint(100, 1000)
        super().save(*args, **kwargs)

    # ----- Computed properties -----

    @property
    def total_likes(self):
        return self.random_likes + self.real_likes

    @property
    def proxied_thumbnail_url(self):
        """Return the proxy URL for the thumbnail if it's a Drive link."""
        if not self.thumbnail_url:
            return ""
        return f"/proxy/media/?url={self.thumbnail_url}"

    @property
    def proxied_audio_url(self):
        """Return the proxy URL for the audio if it's a Drive link."""
        if not self.audio_url:
            return ""
        return f"/proxy/media/?url={self.audio_url}"
