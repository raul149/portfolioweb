from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['raulaznaralvarez.onrender.com','raulaznar.onrender.com','localhost']

INSTALLED_APPS += [    'whitenoise.runserver_nostatic',
    'cloudinary',
    'cloudinary_storage',
]

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get("CLOUDINARY_CLOUD_NAME"),
    'API_KEY': os.environ.get("CLOUDINARY_API_KEY"),
    'API_SECRET': os.environ.get("CLOUDINARY_API_SECRET")
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CSRF_TRUSTED_ORIGINS = ['https://*.127.0.0.1', os.environ.get("HOST_NAME"),'raulaznar.onrender.com']

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
