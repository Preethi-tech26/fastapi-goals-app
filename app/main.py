
# SQLAlchemy, SQLite, database models, persistent storage via POST/GET

# HTTPException, proper status codes, Pydantic validation schemas

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal, Base
from app.models import Goal
from app.schemas import GoalCreate
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.auth import hash_password, verify_password, create_access_token, verify_token
from app.models import User
from app.schemas import UserCreate, Token


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
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    username = verify_token(token)
    if username is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user

@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    new_user = User(username=user.username, hashed_password=hash_password(user.password))
    db.add(new_user)
    db.commit()
    return {"message": f"User {user.username} created successfully"}

@app.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
@app.get("/")
def read_root():
    return {"message": "Welcome to the Goals API"}


@app.post("/goals")
def create_goal(goal: GoalCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_goal = Goal(title=goal.title)
    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)
    return new_goal

@app.get("/goals")
def get_goals(db: Session = Depends(get_db)):
    return db.query(Goal).all()

@app.put("/goals/{goal_id}")
def update_goal(goal_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user), completed: int = None, title: str = None):
    goal = db.query(Goal).filter(Goal.id == goal_id).first()
    if goal is None:
        raise HTTPException(status_code=404, detail="Goal not found")
    if completed is not None:
        goal.completed = completed
    if title is not None:
        goal.title = title
    db.commit()
    db.refresh(goal)
    return goal

from fastapi import FastAPI, Depends, HTTPException

@app.delete("/goals/{goal_id}")
def delete_goal(goal_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    goal = db.query(Goal).filter(Goal.id == goal_id).first()
    if goal is None:
        raise HTTPException(status_code=404, detail="Goal not found")
    db.delete(goal)
    db.commit()
    return {"message": f"Goal {goal_id} deleted"}

