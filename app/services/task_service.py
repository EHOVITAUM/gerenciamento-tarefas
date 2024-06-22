from app.repositories.task_repository import TaskRepository, TaskCreate, TaskUpdate

class TaskService:
    def __init__(self, repository: TaskRepository):
        self._repository = repository

    def create_task(self, task_create: TaskCreate):
        return self._repository.add_task(task_create)

    def get_task(self, task_id: int):
        return self._repository.get_task(task_id)

    def list_tasks(self):
        return self._repository.list_tasks()

    def update_task(self, task_id: int, task_update: TaskUpdate):
        return self._repository.update_task(task_id, task_update)

    def delete_task(self, task_id: int):
        return self._repository.delete_task(task_id)
