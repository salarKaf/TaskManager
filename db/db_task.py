from db.models import ProjectMember
from schemas import TaskBase ,UserAuth
from sqlalchemy.orm import Session
import datetime
from db.models import Task , User
from fastapi.exceptions import HTTPException
from fastapi import Depends
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


