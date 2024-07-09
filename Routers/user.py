from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from schemas import Userdisplay, UserBase,UserAuth
from db import db_user
from db.database import get_db
from auth import oAuth2


router=APIRouter(prefix="/users", tags=['users'])

@router.post("/CreateUser", response_model=Userdisplay)
def create_user(request:UserBase ,db:Session = Depends(get_db)):
    return db_user.create_user(db , request)


@router.get("/GetUser" , response_model=Userdisplay)
def get_User(current_user: UserAuth = Depends(oAuth2.get_current_user) , db:Session = Depends(get_db)):
    return db_user.get_user_by_Id(current_user.id , db)

