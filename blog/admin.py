from django.contrib import admin
from tinymce.widgets import TinyMCE
from django import forms
from .models import Blog


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={"cols": 80, "rows": 30}))

    class Meta:
        model = Blog
        fields = "__all__"


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = ("title", "publish_date", "edit_date", "total_likes")
    list_filter = ("publish_date",)
    search_fields = ("title", "subtitle")
    readonly_fields = ("random_likes",)

    fieldsets = (
        (None, {
            "fields": ("title", "subtitle", "content"),
        }),
        ("Media", {
            "fields": ("thumbnail_url", "audio_url"),
        }),
        ("Engagement", {
            "fields": ("random_likes", "real_likes"),
        }),
        ("Dates", {
            "fields": ("publish_date", "edit_date"),
        }),
    )

    def total_likes(self, obj):
        return obj.total_likes
    total_likes.short_description = "Total Likes"
