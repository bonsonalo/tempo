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
from backend.app.model.models import Users
from backend.app.utils.password_strength import validate_password_strength
from backend.app.core.config import superadmin_dependency



router= APIRouter(
    prefix= "/auth",
    tags= ["auth"]
)

class CreateUserRequest(BaseModel):
    user_name: str
    password: str
    role: str

class Token(BaseModel):
    token_type: str
    access_token: str

    


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")

# for sign up
@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUserRequest, db: db_dependency):
    try:
        validated_password= validate_password_strength(user.password)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="password should include uppercase letter, lowercase letter, special letter and number" )
    
    user_request_model= Users(
        username= user.user_name,
        hashed_password= bcrypt_context.hash(validated_password),
        role= user.role
    )
    db.add(user_request_model)
    db.commit()
    



# for login
@router.post("/login", response_model= Token)
async def login_for_access_token(user_form: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(user_form.username, user_form.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "couldnot validate the user")
    token= create_access_token(user.username, user.id, user.role, timedelta(minutes=20))

    return {"access_token": token, "token_type": "bearer"}

# to upgrade or downgrade a user role

@router.put("/promote/{user_id}")
async def promote_user(id: int, new_role: str, current_user: superadmin_dependency, db: db_dependency):
    user = db.query(Users).filter(Users.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
    user.role = new_role
    db.commit()
    db.refresh(user)
    return {"message": f"User {user.username} promoted to {new_role}"}



def authenticate_user(username: str, password: str, db: db_dependency):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: int, role: str, expires_delta: timedelta):
    encode = {"sub": username, "id": user_id, "role": role}
    expires= datetime.now(timezone.utc) + expires_delta
    encode.update({"exp": expires})

    return jwt.encode(encode, SECRET_KEY, algorithm= ALGORITHM)




