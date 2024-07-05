from db.models import Admin
from schemas import UserBase, AccountRecoveryRequest
from sqlalchemy.orm import Session
from db.hash import Hash
from fastapi.exceptions import HTTPException
from fastapi import status, Depends



def get_token_For_Admin(request:AdminBase , db: Session):
    admin=db.query(Admin).filter(Admin.username==username , Admin.email==username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return user