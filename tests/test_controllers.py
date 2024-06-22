from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_task():
    response = client.post("/tasks/", json={"title": "Test Task", "description": "This is a test task"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "This is a test task"
    assert data["status"] == "Pendente"

def test_get_task():
    # First create a task
    create_response = client.post("/tasks/", json={"title": "Test Task", "description": "This is a test task"})
    task_id = create_response.json()["id"]
    
    # Then get the task
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "This is a test task"
    assert data["status"] == "Pendente"

def test_update_task():
    # First create a task
    create_response = client.post("/tasks/", json={"title": "Old Task", "description": "Old description"})
    task_id = create_response.json()["id"]
    
    # Then update the task
    response = client.put(f"/tasks/{task_id}", json={"title": "Updated Task", "description": "Updated description", "status": "Concluída"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Task"
    assert data["description"] == "Updated description"
    assert data["status"] == "Concluída"

def test_delete_task():
    # First create a task
    create_response = client.post("/tasks/", json={"title": "Task to delete", "description": "This task will be deleted"})
    task_id = create_response.json()["id"]
    
    # Then delete the task
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204
    
    # Verify the task is deleted
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404
