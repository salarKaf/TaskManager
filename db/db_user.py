from db.models import User
from schemas import UserBase
from sqlalchemy.orm import Session
from db.hash import Hash


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

