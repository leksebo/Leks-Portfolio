from .settings import *

DEBUG = True

# Disable all SSL/HTTPS settings
SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = None
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

# Remove SecurityMiddleware
MIDDLEWARE = [m for m in MIDDLEWARE if m != 'django.middleware.security.SecurityMiddleware']

# Disable django-heroku
if 'django_heroku' in globals():
    del django_heroku
