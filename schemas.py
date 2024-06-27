from pydantic import BaseModel
from datetime import datetime
class UserBase(BaseModel):
    username: str
    password: str
    email: str
    name: str

class Userdisplay(BaseModel):
    username: str
    email: str
    name: str
    class Config:
        from_attributes = True

class ProjectBase(BaseModel):
    name: str
    description: str
    creator_id: int
    is_concluded: bool

class User(BaseModel):
    username: str
    class Config:
        from_attributes = True

class ProjectDisplay(BaseModel) :
    name: str
    description: str
    is_concluded: bool
    timestamp: datetime
    user: User
    class Config:
        from_attributes = True

