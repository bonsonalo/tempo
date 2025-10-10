from datetime import timedelta, datetime
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from starlette import status
from .models import Users
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from .config import get_db, db_dependency, SECRET_KEY, ALGORITHM
from typing import Annotated
from datetime import datetime, timezone




router= APIRouter(
    prefix="/auth",
    tags= ["auth"]
)



bcrypt_context= CryptContext(schemes=["bcrypt"], deprecated= "auto")



class CreateUserRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# user sign in
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(create_user_request: CreateUserRequest, db: db_dependency):
    create_user_model= Users(
        username= create_user_request.username,
        hashed_password= bcrypt_context.hash(create_user_request.password)  
    )

    db.add(create_user_model)
    db.commit()


 # user login
@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="could not validate user")
    token = create_access_token(user.username, user.id, timedelta(minutes=20))

    return {"access_token": token, "token_type": "bearer"}



def authenticate_user(username: str, password: str, db: db_dependency):
    user= db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user


def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode= {"sub": username, "id": user_id}
    expires= datetime.now(timezone.utc) + expires_delta 
    encode.update({"exp": expires})

    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


