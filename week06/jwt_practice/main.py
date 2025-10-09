from fastapi import FastAPI, HTTPException, status, Depends
import models
from database import SessionLocal, engine
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel
from config import get_db

app= FastAPI()

models.Base.metadata.create_all(bind= engine)

db_dependency= Annotated[Session, Depends(get_db)]


