from db.models import User
from db.models import Task
from schemas import UserBase
from sqlalchemy.orm import Session
from db.hash import Hash
from fastapi.exceptions import HTTPException
from fastapi import status


def create_user(db: Session, request: UserBase):
    user = User(
        username=request.username,
        name=request.name,
        password=Hash.bcrypt(request.password),
        email=request.email
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user



# def get_all_Projects_Of_User(db: Session):
#     return db.query()

def get_user_by_username(username:str , db: Session):
    user=db.query(User).filter(User.username==username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return user
#
#
# def get_requests_Task(db:Session , username:str):
#     user=db.query(User).filter(User.username==username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
#     return db.query(Task).filter(Task.user_id==user.id & Task.isAccepted==False).all()
#
# def get_tasks(db:Session , username:str):
#     user=db.query(User).filter(User.username==username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
#     return db.query(Task).filter(Task.user_id==user.id & Task.isAccepted==True).all()
#
#
# def get_completed_tasks(db:Session , username:str):
#     user=db.query(User).filter(User.username==username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
#     return db.query(Task).filter(Task.user_id == user.id & Task.is_done == True).all()
#
# def Accept_task(db:Session , username:str , task_id:int):
#     user=db.query(User).filter(User.username==username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
#     else:
#         task=db.query(User).filter(Task.user_id==user.id & Task.id==task_id).first()
#         if not task:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
#         else:
#             if(Task.isAccepted == False):
#                 task.isAccepted = True
#                 db.commit()
#                 db.refresh(task)
#                 return task
#             else:
#                 raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task is accepted before')
#









