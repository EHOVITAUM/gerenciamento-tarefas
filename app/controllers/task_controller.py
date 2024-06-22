from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.task_model import TaskCreate, TaskUpdate, TaskResponse
from app.services.task_service import TaskService
from app.repositories.task_repository import TaskRepository

router = APIRouter()

def get_task_service(db: Session = Depends(get_db)):
    repository = TaskRepository(db)
    return TaskService(repository)

@router.post("/tasks/", response_model=TaskResponse)
def create_task(task_create: TaskCreate, task_service: TaskService = Depends(get_task_service)):
    return task_service.create_task(task_create)

@router.get("/tasks/", response_model=list[TaskResponse])
def list_tasks(task_service: TaskService = Depends(get_task_service)):
    return task_service.list_tasks()

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, task_service: TaskService = Depends(get_task_service)):
    task = task_service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate, task_service: TaskService = Depends(get_task_service)):
    task = task_service.update_task(task_id, task_update)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, task_service: TaskService = Depends(get_task_service)):
    success = task_service.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return None
