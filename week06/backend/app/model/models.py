from backend.app.core.database import base
from sqlalchemy import String, Column, Integer



class User(base):
    __tablename__= "users"

    id= Column(Integer, primary_key=True, index= True)
    username= Column(String, unique=True)
    hashed_password= Column(String)