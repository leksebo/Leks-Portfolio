# LED Portfolio - Django Portfolio Website

## Development Guide

### Local Development

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run migrations:

   ```bash
   python manage.py migrate
   ```

3. Run the development server:
   ```bash
   python manage.py runserver localhost:8000 --settings=led_portfolio.settings_combined
   ```

### Settings Configuration

The project uses different settings for different environments:

- `settings_combined.py`: Main settings file that:
  - Automatically detects development/production environment
  - Configures security settings appropriately
  - Handles static files per environment
  - Uses WhiteNoise for static file serving

### Static Files

Static files are handled differently in development and production:

- Development:

  - Served directly by Django
  - No compression or caching
  - Files served from `portfolio/static/`

- Production:
  - Served by WhiteNoise
  - Compression and caching enabled
  - Files collected to `staticfiles/`
  - Run `python manage.py collectstatic` to collect files

### Environment Variables

- `DJANGO_ENV`: Set to 'production' in production
- `DEBUG`: Controls debug mode
- `DATABASE_URL`: Production database URL (Heroku)
