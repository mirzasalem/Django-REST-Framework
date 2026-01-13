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

## ▶️ Run Project

```bash
pip install django djangorestframework
python manage.py migrate
python manage.py runserver
```

---

## ✨ Author

**Mirza Salem**
