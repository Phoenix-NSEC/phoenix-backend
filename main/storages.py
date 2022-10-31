from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

StaticRootS3Boto3Storage = lambda: S3Boto3Storage(location=settings.STATIC_LOCATION)
MediaRootS3Boto3Storage = lambda: S3Boto3Storage(location=settings.MEDIA_LOCATION)
