from .database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from jose import JWTError, jwt 
from fastapi.security import OAuth2PasswordBearer
from starlette import status



def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency= Annotated[Session, Depends(get_db)]



SECRET_KEY= "222370886cab0b0fc09a75839c9087e31c435307586e27755888952261d0ee95"
ALGORITHM= "HS256" 


oauth2_bearer= OAuth2PasswordBearer(tokenUrl="auth/token")

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload= jwt.decode(token, SECRET_KEY, algorithms= [ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")

        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="could not validate user")
        return {"username": username, "id": user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="could not validate user")
    

user_dependency= Annotated[dict, Depends(get_current_user)]