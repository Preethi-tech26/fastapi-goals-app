# FastAPI Goals App

A REST API built with FastAPI and PostgreSQL to manage personal learning goals, with JWT authentication.

## Live Demo
- API: https://fastapi-goals-app.onrender.com
- Interactive docs: https://fastapi-goals-app.onrender.com/docs

## Features
- User registration and login with JWT authentication
- Create, read, update, and delete personal goals
- Protected endpoints — only authenticated users can modify goals
- Input validation and proper error handling
- Auto-generated interactive API docs (Swagger UI)
- Persistent PostgreSQL database

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL (production) / SQLite (local development)
- JWT (JSON Web Tokens) via python-jose
- Deployed on Render

## Getting Started

### Prerequisites
- Python 3.9+

### Installation
```bash
pip3 install -r requirements.txt
```

### Run the app locally
```bash
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` to explore the API locally.

## API Endpoints

| Method | Endpoint            | Auth Required | Description                        |
|--------|---------------------|---------------|------------------------------------|
| GET    | `/`                 | No            | Health check                       |
| POST   | `/register`         | No            | Register a new user                |
| POST   | `/login`            | No            | Login and receive a JWT token      |
| GET    | `/goals`            | No            | Get all goals                      |
| POST   | `/goals`            | Yes           | Create a new goal                  |
| PUT    | `/goals/{goal_id}`  | Yes           | Update a goal's title or status    |
| DELETE | `/goals/{goal_id}`  | Yes           | Delete a goal                      |

## Authentication

1. Register a new user via `POST /register`
2. Login via `POST /login` with `x-www-form-urlencoded` body
3. Copy the returned `access_token`
4. Add to protected requests as a header:


## About
Built as part of a self-directed learning project transitioning from QA/integration testing into backend development.