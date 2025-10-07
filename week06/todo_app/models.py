from sqlalchemy import Integer, Boolean, ForeignKey, Column, String
from .database import base
from sqlalchemy.orm import relationship


class Todo(base):
    __tablename__= "todo_list"

    id= Column(Integer, primary_key=True, autoincrement=True, index=True)
    todo_text= Column(String, index= True)
    priority= Column(Integer, index=True)
