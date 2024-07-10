from .local_cloud_files import *

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": CREDENTIALS['PGDATABASE'],
        "USER": CREDENTIALS['PGUSER'],
        "PASSWORD": CREDENTIALS['PGPASSWORD'],
        "HOST": CREDENTIALS['PGHOST'],
        "PORT": CREDENTIALS['PGPORT']
    }
}
CONN_MAX_AGE = 60
