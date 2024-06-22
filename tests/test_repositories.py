from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.task_model import Base, Task, TaskCreate, TaskUpdate
from app.repositories.task_repository import TaskRepository

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def test_add_task():
    db = TestingSessionLocal()
    repository = TaskRepository(db)
    task_create = TaskCreate(title="Test Task", description="Test Description")
    task = repository.add_task(task_create)
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.status == "Pendente"
    db.close()

def test_get_task():
    db = TestingSessionLocal()
    repository = TaskRepository(db)
    task_create = TaskCreate(title="Test Task", description="Test Description")
    task = repository.add_task(task_create)
    fetched_task = repository.get_task(task.id)
    assert fetched_task.id == task.id
    assert fetched_task.title == "Test Task"
    db.close()

def test_list_tasks():
    db = TestingSessionLocal()
    repository = TaskRepository(db)
    tasks = repository.list_tasks()
    assert isinstance(tasks, list)
    db.close()

def test_update_task():
    db = TestingSessionLocal()
    repository = TaskRepository(db)
    task_create = TaskCreate(title="Old Task", description="Old Description")
    task = repository.add_task(task_create)
    task_update = TaskUpdate(title="Updated Task", description="Updated Description", status="Concluída")
    updated_task = repository.update_task(task.id, task_update)
    assert updated_task.title == "Updated Task"
    assert updated_task.description == "Updated Description"
    assert updated_task.status == "Concluída"
    db.close()

def test_delete_task():
    db = TestingSessionLocal()
    repository = TaskRepository(db)
    task_create = TaskCreate(title="Task to delete", description="This task will be deleted")
    task = repository.add_task(task_create)
    result = repository.delete_task(task.id)
    assert result is True
    db.close()
