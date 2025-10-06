from fastapi import FastAPI, Query, Path, HTTPException
from typing import Optional
from pydantic import BaseModel, Field


app = FastAPI()


class Priority(BaseModel):
    LOW: 3
    MEDIUM: 2
    HIGH: 1

class TodoBase(BaseModel):
    task: str= Field(..., description="task")
    description: str= Field(..., description= "the description of the task")
    priority: Priority = Field(default=Priority.LOW, description="priority of the task")

class UpdateTodo(BaseModel):
    todo_id: Optional[int]= Field(None, description="Unique id")
    task: Optional[str]= Field(None, description="task")
    description: Optional[str]= Field(None, description= "the description of the task")
    priority: Optional[Priority] = Field(default=Priority.LOW, description="priority of the task")


class Todo(TodoBase):
    todo_id: int= Field(..., description="Unique id")



@app.post('/create-todo/', response_model=Todo)
def create_todo(todo: TodoBase):
    





