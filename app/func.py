from fastapi import HTTPException

def validate_id(todo_id: int):
    if not isinstance(todo_id, int) or todo_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="ID должен быть целым числом больше нуля"
        )
