from .base import *

DEBUG = 'RENDER' not in os.environ

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
