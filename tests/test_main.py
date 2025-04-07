from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_create_todo():
    response = client.post("/todos", json={"id": 1, "item": "task 1"})
    response = client.post("/todos", json={"id": 2, "item": "task 2"})
    assert response.status_code == 200
    assert response.json() == {"message": "Todo has been added"}

def test_get_all_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "item": "task 1"}, {"id": 2, "item": "task 2"}]

def test_get_single_todo():
    response = client.get("/todos/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "item": "task 1"}

def test_get_single_todo_not_found():
    response = client.get("/todos/3")
    assert response.status_code == 404
    assert response.json() == {"detail": "No todos have been found!"}

def test_uptade_todo():
    response = client.put("/todos/2", json={"id": 5, "item": "super task"})
    assert response.status_code == 200
    assert response.json() == {"id": 2, "item": "super task"}

def test_uptade_todo_not_found():
    response = client.put("/todos/5", json={"id": 5, "item": "super task"})
    assert response.status_code == 404
    assert response.json() == {"detail": "No todos found to update"}

def test_delete_todo():
    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo has been deleted"}

def test_delete_todo_not_found():
    response = client.delete("/todos/5")
    assert response.status_code == 404
    assert response.json() == {"detail": "No todos have been found!"}
    response = client.get("/todos")
    assert response.json() == [{"id": 2, "item": "super task"}]