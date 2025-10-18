from .database import SessionLocal
from typing import Annotated, List
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from starlette import status
import os

from dotenv import load_dotenv


load_dotenv()



SECRET_KEY= os.getenv("SECRET_KEY")
ALGORITHM= os.getenv("ALGORITHM")



def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency= Annotated[Session, Depends(get_db)]


oauth_bearer= OAuth2PasswordBearer(tokenUrl="auth/login") # if there was front end, there would have been a ssetup in the front end we dont have to call "auth/token", but since only abckend , when user try to access or request some file, it will tell them to give credentials and then checks that one

def get_current_user(token: Annotated[str, Depends(oauth_bearer)]):
    try:
        payload= jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username:str = payload.get("sub")
        user_id: int= payload.get("id")
        role: str= payload.get("role")

        if username is None or user_id is None or role is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="couldnot be validated")
        return {"username": username, "id": user_id, "role": role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="couldnot be validated")
    

user_authentication_dependency= Annotated[dict, Depends(get_current_user)]


def role_required(allowed_roles: List[str]):
    def wrapper(current_user: user_authentication_dependency):
        user_role= current_user.get("role")
        if not user_role:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User has no role assigned"
            )

        if user_role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission for this action"
            )
        return current_user
    return wrapper

user_dependency= Annotated[dict, Depends(role_required(["user", "admin", "superadmin"]))]
admin_dependency= Annotated[dict, Depends(role_required(["admin", "superadmin"]))]
superadmin_dependency= Annotated[dict, Depends(role_required(["superadmin"]))]
