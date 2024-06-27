from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    password: str
    email:str
    name:str

class Userdisplay(BaseModel):
    username: str
    email: str
    name:str
    class Config:
        from_attributes = True

    class Config:
        from_attributes = True

class ProjectBase(BaseModel):
    name: str
    description: str

