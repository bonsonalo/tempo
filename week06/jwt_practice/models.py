from .database import base
from pydantic import BaseModel
from sqlalchemy import Column, String, Integer

class Users(base):
    __tablename__= 'users'

    id= Column(Integer, primary_key=True, index=True)
    username= Column(String, unique=True)
    hashed_password= Column(String)
