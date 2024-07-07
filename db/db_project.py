import datetime
from db.models import Project , ProjectMember, User , Task
from schemas import ProjectBase , UserAuth , ProjectBaseTask
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from auth import oAuth2

def creat_project(db:Session ,request:ProjectBase ,current_user:UserAuth=Depends(oAuth2.get_current_user) ):
    owner = db.query(User).filter(User.username == current_user.username).first()
    new_project = Project(
        title=request.title,
        description=request.description,
        is_concluded=False,
        timestamp=datetime.datetime.now(),
        owner_id=owner.id
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    new_project_member=ProjectMember(
        user_id=owner.id,
        project_id=new_project.id
    )
    db.add(new_project_member)
    db.commit()
    db.refresh(new_project_member)
    return new_project

def get_all_Projects(db: Session , current_user:UserAuth=Depends(oAuth2.get_current_user)):
    user = db.query(User).filter(User.username == current_user.username).first()
    id_projects=db.query(ProjectMember).filter(ProjectMember.user_id==user.id).all()
    projects = db.query(Project).filter(Project.id.in_([proj.project_id for proj in id_projects])).all()
    return projects


def get_all_Task_In_Project(db: Session , requset: ProjectBaseTask , current_user:UserAuth=Depends(oAuth2.get_current_user) ):
    user = db.query(User).filter(User.username == current_user.username).first()
    pro_mem=db.query(ProjectMember).filter(ProjectMember.project_id==requset.Project_id , ProjectMember.user_id==user.id).first()
    if pro_mem:
        return db.query(Task).filter(Task.project_id == pro_mem.project_id , Task.isAccepted==True).all()

    else:
        raise HTTPException(status_code=404, detail="Not Found")



def get_all_Member_In_Project(db: Session , project_id:int , current_user:UserAuth=Depends(oAuth2.get_current_user)):
    pro_mem=db.query(ProjectMember).filter(ProjectMember.project_id==project_id , ProjectMember.user_id==current_user).first()
    if pro_mem:
        return db.query(ProjectMember).filter(ProjectMember.project_id == project_id).all()

    else:
        raise HTTPException(status_code=404, detail="Not Found")



