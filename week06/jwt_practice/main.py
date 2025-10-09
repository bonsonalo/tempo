from fastapi import FastAPI, HTTPException, status, Depends
from jwt_practice import models
from .database import engine
from .config import db_dependency, user_dependency
from . import auth


app= FastAPI()
app.include_router(auth.router)

models.base.metadata.create_all(bind= engine)



@app.get("/", status_code=status.HTTP_200_OK)
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    return {"user": user}


