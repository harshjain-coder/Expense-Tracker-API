# Expense Tracker API

A RESTful backend API built with Django and Django REST Framework for managing personal expenses.

## Features

- JWT Authentication
- User-based expense management
- Create, Read, Update and Delete expenses
- Expense categories
- Category-based filtering
- Protected APIs
- SQLite database for local development

## Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite
- Git & GitHub

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /api/login/ | User login |
| GET | /api/expenses/ | Get user's expenses |
| POST | /api/expenses/ | Create expense |
| GET | /api/expenses/{id}/ | Get expense |
| PUT | /api/expenses/{id}/ | Update expense |
| DELETE | /api/expenses/{id}/ | Delete expense |

## Run Locally

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Authentication

The API uses JWT authentication. Include the access token as:

Authorization: Bearer <access_token>