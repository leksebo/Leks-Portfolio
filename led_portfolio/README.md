# Personal Portfolio Website

A modern, dynamic portfolio website built with Django, featuring a clean design and easy content management system to showcase my projects and skills as a Software Engineer.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)
- [Contact](#contact)

## About

This portfolio website is designed to showcase my professional work and skills through a modern, responsive interface. It features dynamic content management through Django's admin interface, allowing for easy updates and maintenance of portfolio content.

## Features

- Dynamic content management via Django admin interface
- Responsive design optimized for all devices
- Project showcase with featured projects highlighting
- Rich text editing for project descriptions using TinyMCE
- Integrated contact form using Google Forms
- Skills showcase with animated technology banner
- Clean and modern user interface
- SEO-friendly structure

## Technologies

### Backend

- Django 5.1
- SQLite3
- TinyMCE for rich text editing

### Frontend

- HTML5
- CSS3 with Bootstrap
- JavaScript
- Font Awesome and Bootstrap Icons
- Responsive Design

### Development Tools

- Git & GitHub
- VS Code
- Django Debug Toolbar

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/leksebo/led_portfolio.git
   ```

2. Navigate to the project directory:

   ```bash
   cd led_portfolio
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser to access the admin interface:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

- Access the website at `http://localhost:8000`
- Admin panel: `http://localhost:8000/admin`
  - Manage Personal Information
  - Add/Edit Projects
  - Toggle Featured Projects

## Project Structure

```
led_portfolio/
├── portfolio/                 # Main app directory
│   ├── models.py             # Database models (PersonalInfo, Project)
│   ├── views.py              # View logic
│   ├── urls.py              # URL routing
│   ├── admin.py             # Admin interface customization
│   ├── static/              # Static files (CSS, JS, images)
│   └── templates/           # HTML templates
├── media/                    # User-uploaded files
├── static/                   # Static files
├── staticfiles/             # Collected static files
├── requirements.txt         # Project dependencies
├── Procfile                # Heroku configuration
└── manage.py               # Django management script
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Feel free to reach out to me:

- GitHub: [github.com/leksebo](https://github.com/leksebo)
- LinkedIn: [linkedin.com/in/leks-ebo](https://linkedin.com/in/leks-ebo)
- Contact Form: Available on the website
