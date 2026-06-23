# DRF API project

A Django REST Framework project built to practice and demonstrate modern backend development concepts, including authentication, permissions, testing, background tasks, caching, throttling, and API optimization.

## 🚀 Key Features

### Authentication & Authorization

* User Registration API
* Login API
* Logout API
* Session Authentication
* Token Authentication
* JWT Authentication
* Custom Permissions
* Owner-only update/delete operations

### Performance & Optimization

* Query optimization using `select_related()`
* API Throttling (Rate Limiting)
* Response Caching
* Cache Invalidation on data changes

### Background Tasks

* Redis integration
* Celery worker configuration
* Celery Beat scheduled tasks
* Periodic background jobs

### Quality Assurance

* Unit Tests
* Integration Tests
* API workflow testing
* Permission testing
* Serializer validation testing

### Self-Documenting

* Swagger / Interactive OpenAPI documentation

---

## 🛠️ Tech Stack

* Python 3.13
* Django
* Django REST Framework
* SQLite
* Redis
* Celery
* Celery Beat
* JWT Authentication
* Swagger (drf-yasg)

---

## 📂 API Endpoints

### Authentication

| Method | Endpoint          | Description             |
| ------ | ----------------- | ----------------------- |
| POST   | `/api/register/`  | Register new user       |
| POST   | `/api/login/`     | Login                   |
| POST   | `/api/logout/`    | Logout                  |
| POST   | `/api/token/`     | Obtain DRF Token        |
| POST   | `/token/`         | Obtain JWT Access Token |
| POST   | `/token/refresh/` | Refresh JWT Token       |
| POST   | `swagger/`        | JWT aut settings        |

### Posts

| Method | Endpoint           |
| ------ | ------------------ |
| GET    | `/api/posts/`      |
| POST   | `/api/posts/`      |
| GET    | `/api/posts/<id>/` |
| PUT    | `/api/posts/<id>/` |
| PATCH  | `/api/posts/<id>/` |
| DELETE | `/api/posts/<id>/` |

---

## 📈 Implemented Concepts

This project covers:

* Django REST Framework Setup
* Serializers & Validation
* APIView CRUD
* ViewSets & Routers
* Authentication Systems
* JWT Authentication
* Permissions
* Swagger
* Search, Filter & Pagination
* Unit & Integration Testing
* N+1 Query Optimization
* Redis
* Celery & Celery Beat
* API Throttling
* Response Caching

---

## ▶️ Running the Project

### Clone repository

```bash
git clone <repository-url>
cd drf_normativ
```

### Create virtual environment

```bash
python -m venv .venv
```

### Activate virtual environment

Windows:

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run migrations

```bash
python manage.py migrate
```

### Create superuser

```bash
python manage.py createsuperuser
```

### Run Django server

```bash
python manage.py runserver
```

### Run Redis

```bash
redis-server.exe
```

### Run Celery Worker

```bash
celery -A myproject worker -l info
```

### Run Celery Beat

```bash
celery -A myproject beat -l info
```

---

## 🎯 Project Goal

This project was created as a learning and portfolio to gain hands-on experience with real-world backend development using Django REST Framework and related technologies!

It focuses not only on CRUD operations, but also on authentication, testing, optimization, background processing, caching, and API security.

## 📚 Lessons Learned

During the development of this passionate project, I gained practical experience with several backend development concepts:

* Designing RESTful APIs using Django REST Framework
* Implementing authentication with Sessions, Tokens, and JWT
* Applying permissions to protect resources
* Writing unit and integration tests for API endpoints
* Understanding and solving the N+1 query problem
* Using Redis as a broker and cache backend
* Running asynchronous tasks with Celery
* Scheduling periodic tasks with Celery Beat
* Protecting APIs using throttling (rate limiting)
* Improving performance through response caching
* Reading logs, debugging errors, and troubleshooting integration issues

One of the most valuable lessons was learning how different components of a backend system interact with each other, from database queries and authentication to caching and background task processing. 

Thank you!
