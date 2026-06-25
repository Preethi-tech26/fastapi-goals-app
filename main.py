
# Session 5 - June 2026
# Learned: SQLAlchemy, SQLite, database models, persistent storage via POST/GET


from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from models import Goal

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

@app.post("/goals/{title}")
def create_goal(title: str, db: Session = Depends(get_db)):
    new_goal = Goal(title=title)
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

@app.delete("/goals/{goal_id}")
def delete_goal(goal_id: int, db: Session = Depends(get_db)):
    goal = db.query(Goal).filter(Goal.id == goal_id).first()
    if goal is None:
        return {"error": "Goal not found"}
    db.delete(goal)
    db.commit()
    return {"message": f"Goal {goal_id} deleted"}