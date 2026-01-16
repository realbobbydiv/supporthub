# SupportHub

SupportHub is a small full‑stack ticketing system built as a practical exercise in designing and connecting a real backend, database, and frontend.

The focus of this project is not visual polish, but correctness, structure, and understanding how different parts of a web application work together.

---

## What the app does

- User registration and login using JWT authentication  
- Create, update and assign support tickets  
- Track ticket status and priority  
- Basic ticket statistics (by status and priority)  
- Documented API via Swagger

---

## Tech stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- Alembic (database migrations)
- PostgreSQL (Docker)
- JWT authentication

### Frontend
- React (Vite)
- Axios

---

## Project structure

```
supporthub/
├── backend/        # FastAPI backend
├── frontend/       # React frontend
├── docker-compose.yml
└── README.md
```

---

## Running the project locally

### 1. Start the database

```bash
docker compose up -d
```

### 2. Start the backend

```bash
cd backend
source .venv/bin/activate
uvicorn app.main:app --reload --port 8002
```

Backend will be available at:
- API: http://127.0.0.1:8002
- Docs: http://127.0.0.1:8002/docs

### 3. Start the frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on:
- http://localhost:5173

---

## API overview

- POST /api/auth/register  
- POST /api/auth/login  
- GET /api/users/me  
- POST /api/tickets  
- GET /api/tickets  
- PATCH /api/tickets/{id}  
- GET /api/tickets/stats  

Authentication is handled with JWT.  
The frontend sends the token using the Authorization header.

---

## Why this project exists

This project was built to practice:

- Designing a relational database schema
- Managing schema changes with migrations
- Implementing authentication and protected routes
- Connecting a real frontend to a real backend
- Debugging common development issues (ports, dependencies, API contracts)

---

