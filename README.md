# FastAPI Goals App

A simple REST API built with FastAPI and SQLite to create, read, update, and delete personal learning goals.

## Features

- Create new goals
- View all goals
- Update goal completion status
- Delete goals
- Auto-generated interactive API docs (Swagger UI)

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite

## Getting Started

### Prerequisites

- Python 3.9+

### Installation

\`\`\`bash
pip3 install fastapi uvicorn sqlalchemy
\`\`\`

### Run the app

\`\`\`bash
uvicorn main:app --reload
\`\`\`

Visit `http://127.0.0.1:8000/docs` to explore the API.

## API Endpoints

| Method | Endpoint           | Description            |
| ------ | ------------------ | ---------------------- |
| GET    | `/`                | Health check           |
| POST   | `/goals/{title}`   | Create a new goal      |
| GET    | `/goals`           | Get all goals          |
| PUT    | `/goals/{goal_id}` | Update a goal's status |
| DELETE | `/goals/{goal_id}` | Delete a goal          |

## About

Built as part of a self-directed learning project transitioning from QA/integration testing into backend development.
