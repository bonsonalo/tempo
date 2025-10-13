from fastapi import FastAPI, HTTPException
from backend.app.core import database
from backend.app.core.database import engine
from starlette import status
from backend.app.core.config import db_dependency, user_dependency
from backend.app.api.v1.routes import routers



app= FastAPI()
app.include_router(routers)


database.base.metadata.create_all(bind= engine)
 




    