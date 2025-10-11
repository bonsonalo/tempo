from fastapi import FastAPI, HTTPException
from backend.app.core import database
from backend.app.core.database import engine
from starlette import status
from backend.app.core.config import db_dependency, user_dependency
from backend.app.api.v1.endpoints import auth


app= FastAPI()
app.include_router(auth.router)

database.base.metadata.create_all(bind= engine)


@app.get("/user", status_code=status.HTTP_200_OK)
def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="user not validated")
    return {"User": user}

