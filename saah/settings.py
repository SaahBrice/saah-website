"""
Django settings for saah project.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-$1rkz@x%(=9ec^p*kvd32-l!s5b0n@+hb_-%q^#f)ldqyn%=cz"

DEBUG = True

ALLOWED_HOSTS = ["*"]

# ---------- Apps ----------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party
    "rest_framework",
    "tinymce",
    "drf_spectacular",
    # Local
    "blog",
    "landing",
]

# ---------- Middleware ----------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "saah.urls"

# ---------- Templates ----------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "saah.wsgi.application"

# ---------- Database ----------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ---------- Auth ----------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ---------- i18n ----------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Africa/Douala"
USE_I18N = True
USE_TZ = True

# ---------- Static files ----------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# ---------- Default PK ----------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---------- DRF ----------
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 12,
}

# ---------- drf-spectacular ----------
SPECTACULAR_SETTINGS = {
    "TITLE": "SAAH Blog API",
    "DESCRIPTION": "API for the SAAH library blog — posts, likes, and media proxy.",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

# ---------- TinyMCE ----------
TINYMCE_DEFAULT_CONFIG = {
    "height": 500,
    "width": "100%",
    "menubar": "file edit view insert format tools table help",
    "plugins": (
        "advlist autolink lists link image charmap preview anchor "
        "searchreplace visualblocks code fullscreen "
        "insertdatetime media table paste code help wordcount"
    ),
    "toolbar": (
        "undo redo | formatselect | bold italic underline strikethrough | "
        "forecolor backcolor | alignleft aligncenter alignright alignjustify | "
        "bullist numlist outdent indent | removeformat | link image media | "
        "code fullscreen | help"
    ),
    "content_css": "default",
    "skin": "oxide-dark",
    "content_style": "body { font-family: 'Inter', sans-serif; font-size: 16px; }",
}

# ---------- Site info (used for OG tags) ----------
SITE_NAME = "SAAH"
SITE_DESCRIPTION = "A space built for serious students and workers. Coming to Buea."
SITE_URL = "http://127.0.0.1:8000"
