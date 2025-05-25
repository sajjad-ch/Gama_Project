# Gama_Project
Here’s a **`frontend_setup.md`** file written in markdown to help a frontend developer run and test your Django REST Framework project locally using Postman:

---

# 🧪 Gama Project – Frontend Developer Guide

This guide will help you run the Django backend of the **Gama Project** locally, access the API, and test endpoints using Postman.

---

## 📁 Project Directory Structure

The main project directory looks like this:

```
sajjad-ch-gama_project/
├── Gama/
│   ├── manage.py
│   ├── requirements.txt
│   ├── Gama/
│   ├── institute_module/
│   ├── staff_module/
│   ├── media/
│   ├── statics/
```

---

## 🚀 Step-by-Step Setup

### 1. 📦 Install Requirements

> Make sure you have Python 3.8+ and pip installed.

```bash
cd sajjad-ch-gama_project/Gama
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

### 2. 🛠️ Apply Migrations

```bash
python manage.py migrate
```

---

### 3. 👤 Create Superuser (Optional – for admin login)

```bash
python manage.py createsuperuser
```

---

### 4. 📂 Run the Development Server

```bash
python manage.py runserver
```

Server will be available at:

```
http://127.0.0.1:8000/
```

---

## 📮 API Testing with Postman

### 🔗 Base API URL

```
http://127.0.0.1:8000/api/
```

---

### 📋 Get All Available API URLs

You can automatically view and test all API endpoints if **Django REST Framework’s browsable API** or **drf-spectacular** or **drf-yasg** is installed.

Check one of these:

* `/api/` or `/swagger/` or `/schema/swagger-ui/` – Swagger UI
* `/redoc/` – ReDoc documentation
* `/api-auth/` – DRF login

Otherwise, use this command to list all available URLs (for backend developers):

```bash
python manage.py show_urls
```

> (Make sure `django-extensions` is installed for the command above.)

---

### 🧪 Import to Postman

You can test all APIs using [Postman](https://www.postman.com/):

1. Open Postman
2. Create a new Collection
3. Set base URL: `http://127.0.0.1:8000/api/`
4. Add endpoints manually or use Swagger/OpenAPI JSON to import if available.

---

## 📌 Notes for Frontend

* Media files (e.g. images, resumes) are available under:
  `http://127.0.0.1:8000/media/`

* Admin login:
  `http://127.0.0.1:8000/admin/`

* Some APIs require authentication (token/session). Use login API to obtain credentials.

---

## 🤝 Backend Apps Overview

| App Name           | Purpose                         |
| ------------------ | ------------------------------- |
| `institute_module` | Course info, ranks, suggestions |
| `staff_module`     | HR resumes, collaborations      |
