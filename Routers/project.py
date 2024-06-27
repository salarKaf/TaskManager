from typing import List

from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from schemas import ProjectBase , ProjectDisplay
from db import db_project
from db.database import get_db


router=APIRouter(prefix="/Project", tags=['projects'])

@router.post("", response_model=ProjectDisplay)
def create_project( request:ProjectBase ,db:Session = Depends(get_db)):
    return db_project.creat_project(db , request)


@router.get("/", response_model=List[ProjectDisplay])
def get_project(db:Session = Depends(get_db)):
    return db_project.get_all_Projects(db)

