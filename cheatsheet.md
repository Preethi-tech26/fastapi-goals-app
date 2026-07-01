# My Python & FastAPI Cheat Sheet

Personal reference for things I keep forgetting. Add to this as I learn more.

---

## Terminal / Server

**Start the server:**
```
uvicorn main:app --reload
```

**Check if server is running:**
- Visit `http://127.0.0.1:8000/` in browser, or
```
lsof -i :8000
```

**"Address already in use" error:**
```
lsof -i :8000          # find the PID
kill -9 <PID>          # stop it
uvicorn main:app --reload   # start again
```

**Check if a package is installed:**
```
pip3 show <package_name>
```

---

## Python Basics

**Variables & types:**
```python
name = "Prith"      # string
age = 40            # integer
is_learning = True  # boolean
```

**List:**
```python
goals = ["Learn Python", "Build an API"]
goals[0]   # access first item (starts at 0)
```

**Dictionary (key-value pairs):**
```python
person = {"name": "Prith", "age": 40}
person["name"]   # access by key
```

**If/else:**
```python
if is_learning == True:
    print("Keep going")
else:
    print("Start learning")
```

**Loop through a list:**
```python
for goal in goals:
    print(goal)
```

**Function:**
```python
def greet(name):
    print("Hello", name)

greet("Prith")
```

**Reading/writing files:**
```python
# Write
with open("notes.txt", "w") as file:
    file.write("Hello\n")

# Read
with open("notes.txt", "r") as file:
    contents = file.read()
```

---

## Calling APIs (requests library)

```python
import requests

response = requests.get("https://api.example.com")
data = response.json()   # convert to dictionary
print(response.status_code)
```

---

## FastAPI Basics

**Minimal app:**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello"}
```

**Path parameter:**
```python
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}
```
⚠️ Don't forget the leading `/` before the path name.

**View interactive docs:**
```
http://127.0.0.1:8000/docs
```

---

## Database (SQLAlchemy + SQLite)

**Database setup pattern (database.py):**
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```

**Model = a database table (models.py):**
```python
from sqlalchemy import Column, Integer, String
from database import Base

class Goal(Base):
    __tablename__ = "goals"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Integer, default=0)
```

**Connecting DB to API (main.py):**
```python
from sqlalchemy.orm import Session
from fastapi import Depends

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

**View raw database from terminal:**
```
sqlite3 app.db
SELECT * FROM goals;
.quit
```

**Note:** Deleted IDs are NOT reused — this is normal, not a bug.

---

## CRUD Patterns

| Operation | HTTP Method | Example |
|-----------|-------------|---------|
| Create    | POST        | `@app.post("/goals")` |
| Read      | GET         | `@app.get("/goals")` |
| Update    | PUT         | `@app.put("/goals/{goal_id}")` |
| Delete    | DELETE      | `@app.delete("/goals/{goal_id}")` |

**Find a record or raise 404:**
```python
from fastapi import HTTPException

goal = db.query(Goal).filter(Goal.id == goal_id).first()
if goal is None:
    raise HTTPException(status_code=404, detail="Goal not found")
```
⚠️ Never return `{"error": ...}` with a 200 status — use `raise HTTPException` instead.

---

## Input Validation (Pydantic)

**Schema = rules for valid input (schemas.py):**
```python
from pydantic import BaseModel, Field

class GoalCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
```

**Use in endpoint:**
```python
@app.post("/goals")
def create_goal(goal: GoalCreate, db: Session = Depends(get_db)):
    new_goal = Goal(title=goal.title)
    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)
    return new_goal
```

**Common status codes:**
- `200` — success
- `404` — not found
- `422` — invalid input data (Pydantic validation failure)

---

## Git / GitHub

**First time setup:**
```
git init
git add .
git commit -m "Initial commit"
git remote add origin <repo-url>
git branch -M main
git push -u origin main
```

**Day to day:**
```
git status                 # what's changed
git add .                  # stage changes
git commit -m "message"    # save changes locally
git push                   # send to GitHub
```

**Remove a file from being tracked (but keep it locally):**
```
git rm --cached <filename>
git commit -m "remove file"
git push
```

**Stop a file from ever being tracked again:**
Add it to `.gitignore`:
```
filename.py
```

---

## Debugging Checklist (check these first!)

1. Is the server actually running? (`uvicorn main:app --reload`)
2. Did I save the file?
3. Typo in a URL, route, or variable name?
4. Missing `/` at the start of a route?
5. Right port? (`8000` unless changed)
6. Read the actual error message slowly — it usually tells you exactly what's wrong
