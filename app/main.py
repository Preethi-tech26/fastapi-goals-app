
# Session 5 - June 2026
# Learned: SQLAlchemy, SQLite, database models, persistent storage via POST/GET

# Session 7 - June 2026
# Learned: HTTPException, proper status codes, Pydantic validation schemas

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal, Base
from app.models import Goal
from app.schemas import GoalCreate

app = FastAPI()

# Create the table when the app starts
Base.metadata.create_all(bind=engine)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Hello, Prith"}


@app.post("/goals")
def create_goal(goal: GoalCreate, db: Session = Depends(get_db)):
    new_goal = Goal(title=goal.title)
    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)
    return new_goal

@app.get("/goals")
def get_goals(db: Session = Depends(get_db)):
    return db.query(Goal).all()

@app.put("/goals/{goal_id}")
def update_goal(goal_id: int, completed: int, db: Session = Depends(get_db)):
    goal = db.query(Goal).filter(Goal.id == goal_id).first()
    if goal is None:
        return {"error": "Goal not found"}
    goal.completed = completed
    db.commit()
    db.refresh(goal)
    return goal

from fastapi import FastAPI, Depends, HTTPException

@app.delete("/goals/{goal_id}")
def delete_goal(goal_id: int, db: Session = Depends(get_db)):
    goal = db.query(Goal).filter(Goal.id == goal_id).first()
    if goal is None:
       # return {"error": "Goal not found"}
       raise HTTPException(status_code=404, detail="Goal not found")
    db.delete(goal)
    db.commit()
    return {"message": f"Goal {goal_id} deleted"}


