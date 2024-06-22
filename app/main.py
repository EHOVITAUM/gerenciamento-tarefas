from fastapi import FastAPI
from app.controllers import task_controller
from app.database import init_db

app = FastAPI()

init_db()

app.include_router(task_controller.router)
