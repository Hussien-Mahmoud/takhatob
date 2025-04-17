from .base import *
import os
from google.oauth2 import service_account

# Production-specific settings
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(',')
# CSRF_TRUSTED_ORIGINS = ['https://takhatob-production.up.railway.app', '*']

# Use Google Cloud Storage for media and static files
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage"
    },
    "staticfiles": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage"
    }
}

# Google Cloud Storage settings
GS_BUCKET_NAME = os.environ['gs_bucket_name']
GS_CREDENTIALS = service_account.Credentials.from_service_account_info(
    {
        "type": os.environ["type"],
        "project_id": os.environ["project_id"],
        "private_key_id": os.environ["private_key_id"],
        "private_key": os.environ["private_key"],
        "client_email": os.environ["client_email"],
        "client_id": os.environ["client_id"],
        "auth_uri": os.environ["auth_uri"],
        "token_uri": os.environ["token_uri"],
        "auth_provider_x509_cert_url": os.environ["auth_provider_x509_cert_url"],
        "client_x509_cert_url": os.environ["client_x509_cert_url"],
    }
)
