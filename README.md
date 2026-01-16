# SupportHub

SupportHub is a small full-stack ticketing system built as a learning and portfolio project.
The goal of the project was to understand how a real backend-driven application works end-to-end:
authentication, database design, API logic, and a basic frontend.

This is **not a tutorial clone** – the project was built step by step, debugging and fixing issues along the way,
just like in a real development environment.

---

## Features

- User registration and login using JWT authentication
- Role-aware user context (`/users/me`)
- Create, update and assign support tickets
- Ticket status and priority management
- Ticket statistics endpoint (counts by status and priority)
- REST API with automatic OpenAPI documentation
- PostgreSQL database with Alembic migrations
- Dockerized database
- React frontend connected to the API

---

## Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Docker
- JWT authentication

### Frontend
- React
- Vite
- Axios

---

## Project Structure

