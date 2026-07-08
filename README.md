- User-specific goals — each user can only see and manage their own goals
| Method | Endpoint            | Auth Required | Description                        |
|--------|---------------------|---------------|------------------------------------|
| GET    | `/`                 | No            | Health check                       |
| POST   | `/register`         | No            | Register a new user                |
| POST   | `/login`            | No            | Login and receive a JWT token      |
| GET    | `/goals`            | Yes           | Get current user's goals           |
| POST   | `/goals`            | Yes           | Create a new goal                  |
| PUT    | `/goals/{goal_id}`  | Yes           | Update a goal's title or status    |
| DELETE | `/goals/{goal_id}`  | Yes           | Delete a goal                      |

## About
Built as part of a self-directed learning project transitioning from QA/integration testing 
into backend development. Features full CRUD, JWT authentication, and user-specific data 
isolation on a live PostgreSQL database.