from typing import List
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from auth import oAuth2
from schemas import TaskBase, UserAuth , TaskDisplay
from db import db_task
from db.database import get_db


router=APIRouter(prefix="/Tasks", tags=['Tasks'])

@router.post("", response_model=TaskDisplay)
def create_project( request:TaskBase ,db:Session = Depends(get_db) ,
                    current_user:UserAuth=Depends(oAuth2.get_current_user)):
    return db_task.create_task_and_assign_user(db , request , current_user)


