from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Annotated, Optional, List
from todo_app import models
from config import get_db

from enum import IntEnum
from .database import engine
from sqlalchemy.orm import Session



app = FastAPI()

models.base.metadata.create_all(bind= engine)


class Priority(IntEnum):
    LOW=1
    MEDIUM= 2
    HIGH= 3
class TodoBase(BaseModel):
    todo_text: str
    priority: Priority
class Todofinal(TodoBase):
    id: int

class TodoUpdate(BaseModel):
    todo_text: Optional[str]= None
    priority: Optional[Priority]= None


db_dependency= Annotated[Session, Depends(get_db)]

@app.post("/todo/")
async def create_todo(todo: TodoBase, db: db_dependency):
    db_todo= models.Todo(
        todo_text= todo.todo_text,
        priority= todo.priority
                         )

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)

@app.delete("/todo/{delete_id}")
async def delete_todo(delete_id: int, db: db_dependency):
    db_to_delete= db.query(models.Todo).filter(models.Todo.id == delete_id).first()
    if not db_to_delete:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_to_delete)
    db.commit()

@app.put("/todo/{todo_id}", response_model= Todofinal)
async def edit_todo(todo_id: int, updated_to: TodoUpdate, db: db_dependency):
    db_edit= db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not db_edit:
        raise HTTPException(status_code=404, detail="todo not found")
    else:
        if updated_to.todo_text is not None:
            db_edit.todo_text = updated_to.todo_text
        if updated_to.priority is not None:
            db_edit.priority = updated_to.priority
        db.commit()
        db.refresh(db_edit)
        return db_edit
    


@app.get("/todo/{todo_id}", response_model= Todofinal)
async def get_todo(todo_id: int, db: db_dependency):
    result = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    return result

