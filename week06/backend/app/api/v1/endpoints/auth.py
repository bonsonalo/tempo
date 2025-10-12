from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from pydantic import BaseModel, field_validator
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from starlette import status
from jose import jwt 


from backend.app.core.config import ALGORITHM, SECRET_KEY, db_dependency
from passlib.context import CryptContext
from backend.app.model.models import User
from backend.app.utils.password_strength import validate_password_strength




router= APIRouter(
    prefix= "/auth",
    tags= ["auth"]
)

class CreateUserRequest(BaseModel):
    user_name: str
    password: str

class Token(BaseModel):
    token_type: str
    access_token: str

class Authenticate_user(BaseModel):
    password: str

    @field_validator("password")
    @classmethod
    def password_strength(cls, value):
        return validate_password_strength(value)
    


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")

# for sign up
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUserRequest, db: db_dependency):
    try:
        validated_password= validate_password_strength(user.password)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="password should include uppercase letter, lowercase letter, special letter and number" )
    
    user_request_model= User(
        username= user.user_name,
        hashed_password= bcrypt_context.hash(validated_password)
    )
    db.add(user_request_model)
    db.commit()
    



# for login
@router.post("/token", response_model= Token)
async def login_for_access_token(user_form: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(user_form.username, user_form.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "couldnot validate the user")
    token= create_access_token(user.username, user.id, timedelta(minutes=20))

    return {"access_token": token, "token_type": "bearer"}



def authenticate_user(username: str, password: str, db: db_dependency):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {"sub": username, "id": user_id}
    expires= datetime.now(timezone.utc) + expires_delta
    encode.update({"exp": expires})

    return jwt.encode(encode, SECRET_KEY, algorithm= ALGORITHM)




