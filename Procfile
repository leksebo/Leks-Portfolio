web: cd led_portfolio && DJANGO_SETTINGS_MODULE=led_portfolio.production python manage.py migrate --no-input && python manage.py collectstatic --no-input && gunicorn led_portfolio.wsgi --log-file -
