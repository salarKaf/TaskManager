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

class Project(BaseModel):
    title: str

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


class TaskBaseAccept(BaseModel):
    task_id : int
    project_id: int


class AccountRecoveryRequest(BaseModel):
    email: str


class sent_info_by_email(BaseModel):
    username: str
    password: str
    name: str

class ProjectBaseTask(BaseModel):
    Project_id:int


class AdminBase(BaseModel):
    username: str
    password: str
    email: str
    name: str
    phoneNumber:str


class AdminBaseLogin():
    username: str
    email:str
    phoneNumber:str



class AdminDisplay(BaseModel):
    username: str
    email: str
    name: str

class NoticeBase(BaseModel):
    text: str


class NoticeCreate(NoticeBase):
    team: User
    task: int
    

class Notice(NoticeBase):
    id: int 
    task: int
    isRead:bool 
    team:User

    class Config:
        orm_mode = True