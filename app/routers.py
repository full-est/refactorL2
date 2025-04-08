from fastapi import HTTPException, APIRouter
from .models import Todo, TodoUpdate
from typing import List
from .func import validate_id, duplicate_id


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
    validate_id(todo.id)
    duplicate_id(todo.id, todos)
    todos.append(todo)
    return {"message": "Todo has been added"}

# Update a todo
@routers.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo_obj: TodoUpdate):
    validate_id(todo_id)
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
    validate_id(todo_id)
    for todo in todos:
        if (todo.id == todo_id):
            todos.remove(todo)
            return {"message": "Todo has been deleted"}
    raise HTTPException(status_code=404, detail="No todos have been found!")
