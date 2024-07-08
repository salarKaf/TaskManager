from db.models import User
from schemas import UserBase, AccountRecoveryRequest
from sqlalchemy.orm import Session
from db.hash import Hash
from fastapi.exceptions import HTTPException
from fastapi import status, Depends


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

def get_user_by_username(username:str , db: Session):
    user=db.query(User).filter(User.username==username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return user

def recover_account(db:Session , request: AccountRecoveryRequest):
    user = db.query(User).filter(User.email == request.email).first()
    if user:
        pass
        # # Here you can implement the account recovery logic, such as sending an email with a password reset link
        # return {"message": f"Account recovery initiated for {user_info['full_name']}. Check your email for further instructions."}
    else:
        raise HTTPException(status_code=404, detail="User not found")



def get_user_by_Id(id:int, db: Session):
    user=db.query(User).filter(User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return user














