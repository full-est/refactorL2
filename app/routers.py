from fastapi import HTTPException, APIRouter
from .models import Todo, TodoUpdate
from typing import List


routers = APIRouter()

@routers.get("/")
async def root():
    return {"message": "Hello World"}

todos: List[Todo] = []# empty list


# Get all todos
@routers.get("/todos", response_model=List[Todo])
async def get_todos():
    return todos


# Get single todo
@routers.get("/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    for todo in todos:
        if (todo.id == todo_id):
            return todo
    raise HTTPException(status_code=404, detail="No todos have been found!")

# Create a todo
@routers.post("/todos")
async def create_todos(todo: Todo):
    if todo.id <= 0:
        raise HTTPException(status_code=400, detail="ID должно быть положительным числом")
    todos.append(todo)
    return {"message": "Todo has been added"}

# Update a todo
@routers.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo_obj: TodoUpdate):
    if todo_id <= 0:
        raise HTTPException(status_code=400, detail="ID должно быть положительным числом")
    if not todo_obj.item or len(todo_obj.item.strip()) == 0:
        raise HTTPException(status_code=400, detail="Поле 'item' не может быть пустым")
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return todo
    raise HTTPException(status_code=404, detail="No todos found to update")

# Delete a todo
@routers.delete("/todos/{todo_id}")
async def delete_todos(todo_id: int):
    if todo_id <= 0:
        raise HTTPException(status_code=400, detail="ID должно быть положительным числом")
    for todo in todos:
        if (todo.id == todo_id):
            todos.remove(todo)
            return {"message": "Todo has been deleted"}
    raise HTTPException(status_code=404, detail="No todos have been found!")
