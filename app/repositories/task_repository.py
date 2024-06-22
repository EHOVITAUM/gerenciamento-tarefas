from sqlalchemy.orm import Session
from app.models.task_model import Task, TaskCreate, TaskUpdate

class TaskRepository:
    def __init__(self, db: Session):
        self._db = db

    def add_task(self, task_create: TaskCreate) -> Task:
        task = Task(**task_create.dict())
        self._db.add(task)
        self._db.commit()
        self._db.refresh(task)
        return task

    def get_task(self, task_id: int) -> Task:
        return self._db.query(Task).filter(Task.id == task_id).first()

    def list_tasks(self) -> list[Task]:
        return self._db.query(Task).all()

    def update_task(self, task_id: int, task_update: TaskUpdate) -> Task:
        task = self.get_task(task_id)
        if not task:
            return None
        for key, value in task_update.dict(exclude_unset=True).items():
            setattr(task, key, value)
        self._db.commit()
        self._db.refresh(task)
        return task

    def delete_task(self, task_id: int) -> bool:
        task = self.get_task(task_id)
        if task:
            self._db.delete(task)
            self._db.commit()
            return True
        return False
