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


