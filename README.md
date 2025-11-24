# Login & Signup (Django)

Simple Django app that provides user registration, login, and a protected home page. The UI is kept minimal, using dedicated templates (`index.html`, `Signup.html`, `home.html`) with a shared stylesheet located at `project/projectapp/static/css/auth.css`.

## Features
- Register with full name, email, password confirmation, and role selection.
- Log in with email/password; basic session handling handled in views.
- Home page greets the authenticated user and exposes a logout action.
- SQLite database for persistence (`project/db.sqlite3`).

## Project Layout
```
project/
├── manage.py
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── projectapp/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── static/css/auth.css
    └── templates/
        ├── index.html
        ├── Signup.html
        └── home.html
```

## Getting Started
1. **Install dependencies**
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Apply migrations**
   ```powershell
   py project/manage.py migrate
   ```

3. **Run the development server**
   ```powershell
   py project/manage.py runserver
   ```
   Visit http://127.0.0.1:8000/.

## Static Files
- CSS lives in `project/projectapp/static/css/auth.css`.
- Templates include the stylesheet using `{% load static %}` and `<link rel="stylesheet" href="{% static 'css/auth.css' %}">`.

## Notes
- Default database is SQLite; update `project/project/settings.py` for other databases.
- There is no password hashing or production-grade auth—extend `models.py` and `views.py` if needed before deploying publicly.

