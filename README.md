# LED Portfolio

A modern, dynamic portfolio website built with Django, featuring a clean design and easy content management system to showcase my projects and skills as a Software Engineer.

## Features

- Dynamic content management via Django admin interface
- Responsive design optimized for all devices
- Project showcase with featured projects highlighting
- Rich text editing for project descriptions using TinyMCE
- Integrated contact form
- Skills showcase with animated technology banner
- Environment-specific configurations for development and production
- Secure static file serving with WhiteNoise

## Technologies

- Django 5.1
- PostgreSQL (Production) / SQLite (Development)
- WhiteNoise for static files
- TinyMCE for rich text editing
- Bootstrap for responsive design
- Heroku for deployment

## Quick Start

1. Clone the repository:

   ```bash
   git clone https://github.com/leksebo/led_portfolio.git
   cd led_portfolio
   ```

2. Create and activate virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   cd led_portfolio
   python manage.py migrate
   ```

5. Start development server:

   ```bash
   python manage.py runserver localhost:8000 --settings=led_portfolio.settings_combined
   ```

6. Visit http://localhost:8000 in your browser

## Development vs Production

### Development

- Debug mode enabled
- Static files served directly by Django
- SQLite database
- No SSL enforcement
- Run with: `python manage.py runserver localhost:8000 --settings=led_portfolio.settings_combined`

### Production

- Debug mode disabled
- Static files served by WhiteNoise with compression
- PostgreSQL database
- SSL enforced
- Runs on Heroku with gunicorn
- Environment variable `DJANGO_ENV=production`

## Project Structure

```
Leks Portfolio/
├── led_portfolio/          # Main Django project
│   ├── settings_combined.py  # Combined settings for dev/prod
│   ├── production.py       # Production-specific settings
│   └── wsgi.py            # WSGI configuration
├── portfolio/             # Main Django app
│   ├── static/           # Static files (CSS, JS, images)
│   ├── templates/        # HTML templates
│   ├── models.py         # Database models
│   └── views.py          # View logic
├── staticfiles/          # Collected static files
├── requirements.txt      # Project dependencies
└── Procfile             # Heroku deployment configuration
```

## Configuration

The project uses different settings files:

- `settings_combined.py`: Main settings file that auto-detects environment
- `production.py`: Production-specific settings
- Environment variables control behavior:
  - `DJANGO_ENV`: Set to 'production' in production
  - `DEBUG`: Controls debug mode
  - `DATABASE_URL`: Production database URL

## Static Files

- Development: Served from `portfolio/static/`
- Production:
  - Collected to `staticfiles/`
  - Served by WhiteNoise with compression
  - Run `python manage.py collectstatic` to update

## License

This project is licensed under the MIT License.

## Contact

- GitHub: [github.com/leksebo](https://github.com/leksebo)
- LinkedIn: [linkedin.com/in/leks-ebo](https://linkedin.com/in/leks-ebo)
- Portfolio: [led-portfolio-c2f377f40edc.herokuapp.com](https://led-portfolio-c2f377f40edc.herokuapp.com)
