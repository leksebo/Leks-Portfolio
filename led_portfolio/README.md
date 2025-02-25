# Leks Portfolio

A portfolio website showcasing various projects and allowing users to contact the owner.

## Description

This project is a portfolio website built with Django. It features a clean and modern design to display your projects, personal information, and contact details. Users can browse through your projects, view detailed descriptions, and get in touch with you via a contact form.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/leksebo/led_portfolio.git
   ```
2. Navigate to the project directory:
   ```bash
   cd led_portfolio
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the development server:
   ```bash
   python manage.py runserver
   ```
2. Access the website at `http://127.0.0.1:8000/`.

## Features

- **Personal Information**: Display your name, role, and a brief bio.
- **Projects**: Showcase your projects with titles, descriptions, images, and links.
- **Featured Projects**: Highlight specific projects on the homepage.
- **Contact Form**: Allow users to send you messages directly from the website.
- **Admin Interface**: Manage your projects and personal information through the Django admin panel.

## Project Structure

```
assets/
    CSS/
        style.css
    Images/
    JavaScript/
        app.js
led_portfolio/
    db.postgres
    db.sqlite3
    led_portfolio/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    manage.py
    portfolio/
        __init__.py
        admin.py
        apps.py
        forms.py
        models.py
        static/
        templates/
        tests.py
    portfolio_data.json
media/
    projects/
staticfiles/
    admin/
    CSS/
    JavaScript/
    portfolio/
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
