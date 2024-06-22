from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.task_model import Base, TaskCreate, TaskUpdate
from app.repositories.task_repository import TaskRepository
from app.services.task_service import TaskService

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def test_create_task():
    db = TestingSessionLocal()
    repository = TaskRepository(db)
    service = TaskService(repository)
    task_create = TaskCreate(title="Service Test Task", description="Service Test Description")
    task = service.create_task(task_create)
    assert task.title == "Service Test Task"
    assert task.description == "Service Test Description"
    db.close()

def test_get_task():
    db = TestingSessionLocal()
    repository = TaskRepository(db)
    service = TaskService(repository)
    task_create = TaskCreate(title="Service Test Task", description="Service Test Description")
    task = service.create_task(task_create)
    fetched_task = service.get_task(task.id)
    assert fetched_task.id == task.id
    assert fetched_task.title == "Service Test Task"
    db.close()

def test_list_tasks():
    db = TestingSessionLocal()
    repository = TaskRepository(db)
    service = TaskService(repository)
    tasks = service.list_tasks()
    assert isinstance(tasks, list)
    db.close()

def test_update_task():
    db = TestingSessionLocal()
    repository = TaskRepository(db)
    service = TaskService(repository)
    task_create = TaskCreate(title="Old Service Task", description="Old Service Description")
    task = service.create_task(task_create)
    task_update = TaskUpdate(title="Updated Service Task", description="Updated Service Description", status="Concluída")
    updated_task = service.update_task(task.id, task_update)
    assert updated_task.title == "Updated Service Task"
    assert updated_task.description == "Updated Service Description"
    assert updated_task.status == "Concluída"
    db.close()

def test_delete_task():
    db = TestingSessionLocal()
    repository = TaskRepository(db)
    service = TaskService(repository)
    task_create = TaskCreate(title="Service Task to delete", description="This task will be deleted")
    task = service.create_task(task_create)
    result = service.delete_task(task.id)
    assert result is True
    db.close()
