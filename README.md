# 🚀 Django REST API – Person Management System

A Django REST Framework (DRF) based backend application that provides **user authentication** and **CRUD APIs** for managing people and their associated countries.

---

## 📌 Features

- User Registration & Login
- Token-based Authentication
- CRUD operations for Person
- Country relationship with nested serialization
- APIView, Function-Based Views & ViewSets
- Search functionality
- Custom serializer validations

---

## 🛠️ Tech Stack

- Python 3.x
- Django
- Django REST Framework
- SQLite / MySQL
- Token Authentication

---

## 📂 Project Structure

```
project/
│
├── home/
│   ├── views.py
│   ├── serializers.py
│   ├── models.py
│   └── urls.py
│
├── core/
│   └── settings.py
│
├── manage.py
└── README.md
```

---

## 🔑 Authentication

Add token to headers:

```
Authorization: Token YOUR_TOKEN
```

---

## 📌 API Endpoints

### Register
**POST** `/register/`

```json
{
  "username": "mirza",
  "email": "mirza@gmail.com",
  "password": "123456"
}
```

---

### Login
**POST** `/login/`

```json
{
  "username": "mirza",
  "password": "123456"
}
```

---

## 👤 Person API (Protected)

### Get All Persons
**GET** `/persons/`

### Create Person
**POST** `/persons/`

```json
{
  "name": "John",
  "age": 25,
  "country": 1
}
```

### Update Person
**PATCH** `/persons/`

```json
{
  "id": 1,
  "age": 30
}
```

### Delete Person
**DELETE** `/persons/`

```json
{
  "id": 1
}
```

---

# ⚙️ Additional Project Configuration Documentation

This document describes **extra configurations** added to the Django project beyond the default setup.

---

## 🗄️ Database Configuration (MySQL)

The project uses **MySQL** instead of SQLite.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'course_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### Requirements
- MySQL Server installed and running
- Database name: `course_db`
- Python MySQL client:
```bash
pip install mysqlclient
```

---

## 🔐 Django REST Framework Setup

### Installed Apps
```python
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
]
```

---

### Authentication Configuration
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```

- Supports Basic Authentication
- Supports Session Authentication

---

### Permission Policy
```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
```

- APIs are publicly accessible by default
- Individual views may override permissions

---

### Pagination
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}
```

- Pagination enabled using LimitOffsetPagination
- Default page size: 100

---

## 🧪 Development Settings

```python
DEBUG = True
```

⚠️ Debug mode is enabled for development only.

---

## 🔐 Security Notes

- `SECRET_KEY` is hardcoded for development
- `ALLOWED_HOSTS` is empty
- Move sensitive data to environment variables for production

---

## ⚠️ Important Note

Multiple `REST_FRAMEWORK` configurations exist in `settings.py`.  
They should be **merged into a single dictionary** in production.

---

## 🚀 Recommended Improvements

- Enable TokenAuthentication globally
- Use `.env` file for secrets
- Add Swagger / OpenAPI documentation
- Add CORS support for frontend integration

---

## ✨ Author

**Mirza Salem**
