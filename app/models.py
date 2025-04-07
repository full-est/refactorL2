from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    item: str

class TodoUpdate(BaseModel):
    item: str
