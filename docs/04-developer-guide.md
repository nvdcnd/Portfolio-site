---
title: Developer & Setup Guide
version: 1.0.0
status: Stable
---

# Purpose

This document provides setup instructions for new developers and AI agents working on this project.

It outlines environment creation, dependency installation, database migration, and test execution.

Following this guide ensures a consistent development setup and prevents configuration errors.



# System Requirements

- Python 4.2 (or Python 3.10+)

- PostgreSQL (Neon instance or local server)

- Cloudinary Account (for media uploads)

- Virtual Environment tool (`venv`)



# Local Setup Steps

Step 1: Clone the Repository

- Clone the project repository to your local directory.

Step 2: Create a Virtual Environment

- Run `python -m venv venv` in the root folder.

Step 3: Activate the Virtual Environment

- Windows: `venv\Scripts\activate`

- macOS / Linux: `source venv/bin/activate`

Step 4: Install Dependencies

- Run `pip install -r requirements.txt` (or install dependencies from `requirements/` folder if split).



# Environment Configuration

Create a `.env` file in the `porifolio_site/` directory (where `manage.py` resides).

Example Config

```
SECRET_KEY=your-django-secret-key-here

DEBUG=True

ALLOWED_HOSTS=localhost,127.0.0.1

DATABASE_URL=postgres://user:password@host:port/dbname

CLOUDINARY_CLOUD_NAME=your-cloudinary-cloud-name

CLOUDINARY_API_KEY=your-cloudinary-api-key

CLOUDINARY_API_SECRET=your-cloudinary-api-secret
```

Never commit the `.env` file to version control. The `.gitignore` must exclude it.



# Database Setup

Step 1: Apply Migrations

- Run `python manage.py migrate` to create database tables.

Step 2: Create Superuser

- Run `python manage.py createsuperuser` and follow prompts to create an admin account.

Step 3: Verify Admin Panel

- Start the server and navigate to `http://127.0.0.1:8000/admin/` to verify login.



# Seed Data (Fixtures)

To load sample structured data for development, run:

```
python manage.py loaddata sample_data.json
```

If sample data fixtures are split by application, run:

```
python manage.py loaddata apps/core/fixtures/sample_core.json
```

Never run seed scripts on a production database unless verified.



# Launch Development Server

To launch the local web server, run:

```
python manage.py runserver
```

Open a web browser and navigate to `http://127.0.0.1:8000/` to view the running application.



# Code Style & Formatting

Code Formatting

- Python code must conform to Black formatting rules.

- HTML, CSS, and JS must use double-space indents.

Imports

- Organize imports: Standard libraries first, third-party packages second, local application modules third.

Linting

- Run linters before committing code: `flake8` or `pylint`.



# Executing Tests

To run the Django test suite, execute:

```
python manage.py test
```

To run tests with code coverage:

```
coverage run manage.py test

coverage report -m
```

Ensure all tests pass before proposing code updates.



# Definition of Done for Features

Before marking a task as done:

✓ All unit tests pass.

✓ Gunicorn and WhiteNoise build without errors.

✓ Admin models are registered and tested.

✓ Media files upload successfully to Cloudinary.

✓ Code is formatted according to standard rules.
