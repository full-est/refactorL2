from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Get all todos

# Get single todo

# Create a todo

# Update a todo

# Delete a todo