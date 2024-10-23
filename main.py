from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = [] # empty list


# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}


# Get single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if (todo.id == todo_id):
            return {"todo": todo}
    return {"message": "No todos have been found!"}

# Create a todo
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message": "Todo has been added"}

# Update a todo

# Delete a todo


@app.delete("/todos/{todo_id}")
async def delete_todos(todo_id: int):
    for todo in todos:
        if (todo.id == todo_id):
            todos.remove(todo)
            return {"message": "Todo has been deleted"}
    return {"message": "No todos have been found!"}
