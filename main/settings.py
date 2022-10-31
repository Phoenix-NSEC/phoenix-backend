"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import os
from urllib.parse import urlparse
import dj_database_url
import json
from google.oauth2 import service_account
from django import __version__ as DJANGO_VERSION
from rest_framework import VERSION as REST_FRAMEWORK_VERSION

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"


if DEBUG:
    ALLOWED_HOSTS = ["*"]
    CLOUDRUN_SERVICE_URL = "http://localhost:8000"
else:
    CLOUDRUN_SERVICE_URL = os.getenv("CLOUDRUN_SERVICE_URL")
    ALLOWED_HOSTS = [
        urlparse(CLOUDRUN_SERVICE_URL).netloc,
        "api.admin.phoenixnsec.in",
        "api.phoenixnsec.in",
    ]

    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (
    "http://localhost:3000",
    "http://admin.phoenixnsec.in",
    "https://admin.phoenixnsec.in",  # for network
    "http://phoenixnsec.in",
    "https://phoenixnsec.in",
    "http://www.phoenixnsec.in",
    "https://www.phoenixnsec.in",
)

CSRF_TRUSTED_ORIGINS = [
    CLOUDRUN_SERVICE_URL,
    "http://localhost:3000",
    "http://*.phoenixnsec.in",
    "https://*.phoenixnsec.in",  # for network
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "django_filters",
    "drf_spectacular",
    "user",
    "admin_panel",
    "member",
]

AUTH_USER_MODEL = "user.User"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "main.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": os.getenv("POSTGRES_DB"),
    #     "USER": os.getenv("POSTGRES_USER"),
    #     "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
    #     "HOST": os.getenv("POSTGRES_HOST"),
    #     "PORT": os.getenv("POSTGRES_PORT"),
    # }
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL"), engine="django_cockroachdb"
    )
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ),
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAdminUser",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 20,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Phoenix Backend",
    "DESCRIPTION": f"""
    # Phoenix's Backend Written in Django.
    Django Version: {DJANGO_VERSION}
    DRF Version: {REST_FRAMEWORK_VERSION}
    """,
    "VERSION": "0.1.0b",
    "SERVE_INCLUDE_SCHEMA": False,
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAdminUser"],
    "COMPONENT_SPLIT_REQUEST": True,
    "SCHEMA_PATH_PREFIX": r"/api/v[0-9]",
    "CONTACT": {"name": "Phoenix NSEC", "url": "https://phoenixnsec.in"},
    "LICENSE": {"name": "MIT"},
    # "SWAGGER_UI_DIST": "https://unpkg.com/swagger-ui-dist@4.15.2/"
    # OTHER SETTINGS
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=365),
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "UPDATE_LAST_LOGIN": False,
}

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True

# File Storage
DEFAULT_FILE_STORAGE = "main.storages.MediaRootS3Boto3Storage"
STATICFILES_STORAGE = "main.storages.StaticRootS3Boto3Storage"

AWS_ACCESS_KEY_ID = os.getenv("AWS_S3_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_S3_SECRET_ACCESS_KEY")

AWS_STORAGE_BUCKET_NAME = "phoenix-nsec"

STATIC_LOCATION = "static"
MEDIA_LOCATION = "media"

STATIC_URL = "https://{}.s3.fr-par.scw.cloud/{}/".format(
    AWS_STORAGE_BUCKET_NAME, STATIC_LOCATION
)
MEDIA_URL = "https://{}.s3.fr-par.scw.cloud/{}/".format(
    AWS_STORAGE_BUCKET_NAME, MEDIA_LOCATION
)
AWS_S3_REGION_NAME = "fr-par"
AWS_DEFAULT_ACL = "public-read"
AWS_S3_ENDPOINT_URL = "https://s3.fr-par.scw.cloud"
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
