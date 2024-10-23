from fastapi import FastAPI

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

# Create a todo

# Update a todo

# Delete a todo