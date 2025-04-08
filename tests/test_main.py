from fastapi.testclient import TestClient
from fastapi import HTTPException
import pytest
from app.main import app
from app.func import validate_id

client = TestClient(app)

def test_validate_id_valid():
        validate_id(1)
def test_validate_id_zero():
    with pytest.raises(HTTPException) as exc_info:
        validate_id(0)
    assert exc_info.value.status_code == 400
    assert "ID должен быть целым числом больше нуля" in exc_info.value.detail

def test_validate_id_negative():
    with pytest.raises(HTTPException) as exc_info:
        validate_id(-5)
    assert exc_info.value.status_code == 400
    assert "ID должен быть целым числом больше нуля" in exc_info.value.detail

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_create_todo():
    response = client.post("/todos", json={"id": 1, "item": "task 1"})
    response = client.post("/todos", json={"id": 2, "item": "task 2"})
    assert response.status_code == 200
    assert response.json() == {"message": "Todo has been added"}
    response = client.delete("/todos/1")
    response = client.delete("/todos/2")

def test_create_invalid_todo():
    response = client.post("/todos", json={"id": -2, "item": "task"})
    assert response.status_code == 400
    assert response.json() == {"detail": "ID должен быть целым числом больше нуля"}

def test_get_all_todos():
    response = client.post("/todos", json={"id": 1, "item": "task 1"})
    response = client.post("/todos", json={"id": 2, "item": "task 2"})
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "item": "task 1"}, {"id": 2, "item": "task 2"}]

def test_get_single_todo():
    response = client.post("/todos", json={"id": 1, "item": "task 1"})
    response = client.get("/todos/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "item": "task 1"}

def test_get_single_todo_not_found():
    response = client.get("/todos/3")
    assert response.status_code == 404
    assert response.json() == {"detail": "No todos have been found!"}

def test_uptade_todo():
    response = client.post("/todos", json={"id": 2, "item": "efwfwfw"})
    response = client.put("/todos/2", json={"item": "super task"})
    assert response.status_code == 200
    assert response.json() == {"id": 2, "item": "super task"}

def test_uptade_todo_not_found():
    response = client.put("/todos/5", json={"item": "super task"})
    assert response.status_code == 404
    assert response.json() == {"detail": "No todos found to update"}

def test_update_invalid_todo():
     response = client.put("/todos/-1", json={"item": "task"})
     assert response.status_code == 400
     assert response.json() == {"detail": "ID должен быть целым числом больше нуля"}
     response = client.put("/todos/1", json={"item": ""})
     assert response.status_code == 400
     assert response.json() == {"detail": "Поле 'item' не может быть пустым"}


def test_delete_todo():
    response = client.post("/todos", json={"id": 4, "item":"fdsfs"})
    response = client.delete("/todos/4")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo has been deleted"}

def test_delete_todo_not_found():
    response = client.delete("/todos/5")
    assert response.status_code == 404
    assert response.json() == {"detail": "No todos have been found!"}

def test_delete_invalid_todo():
    response = client.delete("/todos/-23")
    assert response.status_code == 400
    assert response.json() == {"detail": "ID должен быть целым числом больше нуля"}