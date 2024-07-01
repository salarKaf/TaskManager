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

class User(BaseModel):
    username: str
    class Config:
        from_attributes = True

class ProjectDisplay(BaseModel) :
    title: str
    description: str
    is_concluded: bool
    timestamp: datetime
    owner: User
    class Config:
        from_attributes = True

class UserAuth (BaseModel):
    user_id: int
    username: str
    email: str
    name: str

class ProjectBase(BaseModel):
    title: str
    description: str
    # creator_id: int
    is_concluded: bool



class TaskBase(BaseModel):
    title : str
    description : str
    user_id: int
    project_id: int


class TaskDisplay(BaseModel):
    title: str
    description: str
    is_done: bool
    isAccepted: bool
    timestamp: datetime
    user: User
    project: ProjectDisplay
    class Config:
        from_attributes = True










