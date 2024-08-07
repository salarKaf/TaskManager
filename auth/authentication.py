from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from db import models
from db.database import get_db
from db.hash import Hash
from auth import oAuth2
from fastapi.exceptions import HTTPException


router = APIRouter(tags=['authentication'])

@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends() , db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.username==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='invalid credential')

    if not Hash.verify(user.password , request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='invalid password')


    access_token=oAuth2.create_access_token(data={'sub': request.username})
    return {
        'access_token': access_token,
        'token_type':'bearer',
        'userID': user.id,
        'username': user.username,
    }


