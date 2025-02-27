from .settings import *

# Override debug setting
DEBUG = False

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Static files configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
WHITENOISE_USE_FINDERS = True
WHITENOISE_MANIFEST_STRICT = False
WHITENOISE_ALLOW_ALL_ORIGINS = True

# Database configuration
db_from_env = dj_database_url.config(
    conn_max_age=600,
    ssl_require=True
)
DATABASES['default'].update(db_from_env)

# Cache configuration
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Ensure HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Fix sqlite3 issue on Heroku
options = DATABASES['default'].get('OPTIONS', {})
options.pop('sslmode', None)

# Allow all host headers
ALLOWED_HOSTS = [
    'ancient-lemongrass-qi16rk8xa0ohhqf71fha6vba.herokudns.com',
    'led-portfolio-c2f377f40edc.herokuapp.com',
    '.herokuapp.com',
    '*'  # For development - remove in strict production
]
