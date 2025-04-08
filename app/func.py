from fastapi import HTTPException
from typing import List
from .models import Todo


def validate_id(todo_id: int):
    if not isinstance(todo_id, int) or todo_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="ID должен быть целым числом больше нуля"
        )

def duplicate_id(todo_id, todos: List[Todo]):
    if any(todo.id == todo_id for todo in todos):
            raise HTTPException(
                status_code=400,
                detail="Todo с таким ID уже существует"
            )