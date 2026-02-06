from fastapi import FastAPI, Depends, HTTPException
from typing import List
from .models import Task, TaskCreate
from .repositories import InMemoryTaskRepository, ITaskRepository, SqlTaskRepository
from .services import TaskService
from .database import SessionLocal
from sqlalchemy.orm import Session
from . import models_orm
from .database import engine

models_orm.Base.metadata.create_all(bind=engine)
app = FastAPI()



# Singleton Repository Instance
#task_repo = InMemoryTaskRepository()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Dependency Provider
# def get_task_service():
#     return TaskService(task_repo)
def get_task_service(db: Session = Depends(get_db)):
    repo = SqlTaskRepository(db)
    return TaskService(repo)

@app.get("/tasks", response_model=List[Task])
def read_tasks(service: TaskService = Depends(get_task_service)):
    return service.get_tasks()

@app.post("/tasks", response_model=Task)
def create_task(
    task: TaskCreate, 
    service: TaskService = Depends(get_task_service)
):
    return service.create_task(task)

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(
    task_id: int,
    task_in: TaskCreate,
    service: TaskService = Depends(get_task_service)
):
    existing_task = service.repo.get_by_id(task_id)
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    updated_task = Task(
        id=task_id,
        title=task_in.title,
        description=task_in.description,
        completed=task_in.completed
    )
    return service.update_task(updated_task)