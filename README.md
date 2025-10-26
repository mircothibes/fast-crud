# 🐳 fast-crud

A simple CRUD application built with **FastAPI**, **PostgreSQL**, and **Docker Compose**.  
The project demonstrates how to create a modular backend using Python with SQLAlchemy ORM, environment configuration via `.env`, and container orchestration through Docker Compose.

---

## 📘 Overview

The `fast-crud` project provides a small REST API that manages **users** with the following operations:

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/` | GET | Root message |
| `/health` | GET | Health check |
| `/users` | POST | Create a new user |
| `/users` | GET | List all users |
| `/users/{id}` | GET | Get user by ID |
| `/users/{id}` | PUT | Update user info |
| `/users/{id}` | DELETE | Delete user |

---

## ⚙️ Tech Stack

- 🐍 **Python 3.12**
- ⚡ **FastAPI** — modern web framework for building APIs
- 🗃️ **PostgreSQL 16** — relational database
- 🧱 **SQLAlchemy ORM**
- 🐳 **Docker & Docker Compose**
- 🧩 **Pydantic v2** for validation
- 🧠 **Uvicorn** as ASGI server

---

## 🧩 Project Structure

```bash
fast-crud/
├── app/
│ ├── crud/
│ │ └── user.py
│ ├── models/
│ │ └── user.py
│ ├── routers/
│ │ └── users.py
│ ├── schemas/
│ │ └── user.py
│ ├── database.py
│ └── main.py
├── Dockerfile
├── docker-compose.yml
├── .env
├── requirements.txt
└── README.md
```

---

## 🐳 Docker Compose Setup

Two containers are created:

- fast-crud-db → PostgreSQL database
- fast-crud-api → FastAPI application

---

## 🧱 Build and Run
```bash
# Build and start containers
docker compose up --build
```

Once running:

- API: http://localhost:8000
- Docs: http://localhost:8000/docs

---

## 🔍 API Quick Test (cURL)
```bash

# Create a user
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Ana","email":"ana@example.com"}'

# List all users
curl http://localhost:8000/users

# Get user by ID
curl http://localhost:8000/users/1

# Update a user
curl -X PUT http://localhost:8000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Ana Maria","email":"ana.maria@example.com"}'

# Delete a user
curl -X DELETE http://localhost:8000/users/1 -i
```

---

## 📦 Dependencies (requirements.txt)
```bash
fastapi
uvicorn[standard]
sqlalchemy
psycopg2-binary
python-dotenv
pydantic
email-validator
```

---

## 📘 Learnings and Highlights
```bash
✅ Python + FastAPI CRUD structure
✅ Environment management with .env
✅ PostgreSQL database connection via SQLAlchemy
✅ Docker Compose orchestration (multi-container setup)
✅ Health checks and service dependencies
✅ Modular codebase: models, schemas, crud, routers
```

---

## 🧑‍💻 Author

Marcos Vinicius Thibes Kemer
