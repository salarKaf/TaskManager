import datetime
from db.models import Project
from schemas import ProjectBase
from sqlalchemy.orm import Session


def creat_project(db :Session , request:ProjectBase):
    new_project = Project(
        name=request.name,
        description=request.description,
        is_concluded=request.is_concluded,
        timestamp=datetime.datetime.now(),
        user_id=request.creator_id
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

def get_all_Projects(db: Session):
    return db.query(Project).all()

