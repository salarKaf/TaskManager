import datetime
from db.models import Project , ProjectMember, User
from schemas import ProjectBase , UserAuth
from sqlalchemy.orm import Session
from fastapi import Depends
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



