from pydantic import BaseModel, Field

class GoalCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    
class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=6)

class Token(BaseModel):
    access_token: str
    token_type: str