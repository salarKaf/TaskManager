from typing import List
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from auth import oAuth2
from schemas import TaskBase, UserAuth , TaskDisplay , TaskBaseAccept, TaskBaseDone
from db import db_task
from db.database import get_db


router=APIRouter(prefix="/Tasks", tags=['Tasks'])

@router.post("", response_model=TaskDisplay)
def create_project( request:TaskBase ,db:Session = Depends(get_db) ,
                    current_user:UserAuth=Depends(oAuth2.get_current_user)):
    return db_task.create_task_and_assign_user(db , request , current_user)

@router.get("/get Request", response_model=List[TaskDisplay])
def get_requests_Task(db:Session = Depends(get_db) , current_user:UserAuth=Depends(oAuth2.get_current_user)):
    return db_task.get_requests_Task(db ,current_user)


@router.get("/get Task", response_model=List[TaskDisplay])
def get_Tasks(db:Session = Depends(get_db) , current_user:UserAuth=Depends(oAuth2.get_current_user)):
    return db_task.get_Tasks(db ,current_user)

@router.get("/get completed Task", response_model=List[TaskDisplay])
def get_completed_Task(db:Session = Depends(get_db) , current_user:UserAuth=Depends(oAuth2.get_current_user)):
    return db_task.get_completed_Task(db ,current_user)

@router.post("/Accept task", response_model=TaskDisplay)
def Accept_task(request: TaskBaseAccept, db: Session = Depends(get_db),
                       current_user: UserAuth = Depends(oAuth2.get_current_user)):
    return db_task.Accept_task(db ,request,current_user)


# @router.post("\Complete Task" , response_model=TaskDisplay)
# def Done_Task(request: TaskBaseDone, db: Session = Depends(get_db),
#                        current_user: UserAuth = Depends(oAuth2.get_current_user)):
#     return db_task.Done_task(db ,request,current_user)