from db.models import ProjectMember , Project
from schemas import TaskBase ,UserAuth , TaskBaseAccept
from sqlalchemy.orm import Session
import datetime
from db.models import Task , User
from fastapi.exceptions import HTTPException
from fastapi import Depends , status
from auth import oAuth2
def create_task_and_assign_user(db :Session , request:TaskBase , current_user:UserAuth=Depends(oAuth2.get_current_user)):
    owner = db.query(User).filter(User.username == current_user.username).first()
    pro_User = db.query(ProjectMember).filter( ProjectMember.project_id == request.project_id , ProjectMember.user_id == owner.id).first()
    user=db.query(User).filter(User.id == request.user_id).first()
    if user:
        if pro_User:
            new_task = Task(
            title = request.title,
            description = request.description,
            is_done = False,
            timestamp = datetime.datetime.now(),
            project_id = request.project_id,
            user_id=request.user_id,
            isAccepted=False

            )
            db.add(new_task)
            db.commit()
            db.refresh(new_task)

            new_projectMember=ProjectMember(project_id=request.project_id ,
                                            user_id=request.user_id)

            db.add(new_projectMember)
            db.commit()
            db.refresh(new_projectMember)

            return new_task

        else:
            raise HTTPException(status_code=404, detail="This project is not belong to current User!")
    else:
        raise HTTPException(status_code=404, detail="User not found")



def get_requests_Task(db:Session , current_user:UserAuth=Depends(oAuth2.get_current_user)):
    user = db.query(User).filter(User.username == current_user.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return db.query(Task).filter(Task.user_id==user.id , Task.isAccepted==False).all()


def get_Tasks(db:Session , current_user:UserAuth=Depends(oAuth2.get_current_user)):
    user = db.query(User).filter(User.username == current_user.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return db.query(Task).filter(Task.user_id==user.id , Task.isAccepted==True).all()

def get_completed_Task(db:Session , current_user:UserAuth=Depends(oAuth2.get_current_user)):
    user = db.query(User).filter(User.username == current_user.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return db.query(Task).filter(Task.user_id==user.id , Task.is_done==True).all()



def Accept_task(db:Session , request:TaskBaseAccept ,current_user:UserAuth=Depends(oAuth2.get_current_user)):
    user = db.query(User).filter(User.username == current_user.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    else:
        task = db.query(Task).filter(Task.user_id == user.id, Task.project_id==request.project_id , Task.id==request.task_id).first()
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
        else:
            if (task.isAccepted == False):
                task.isAccepted = True
                db.commit()
                db.refresh(task)
                return task
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task is accepted before')


def Done_task(db:Session , request:TaskBaseAccept ,current_user:UserAuth=Depends(oAuth2.get_current_user)):
    user = db.query(User).filter(User.username == current_user.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    else:
        task = db.query(Task).filter(Task.user_id == user.id, Task.project_id==request.project_id , Task.id==request.task_id).first()
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
        else:
            if (task.isAccepted == True):
                task.is_done=True
                db.commit()
                db.refresh(task)
                return task
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task is not accepted')
