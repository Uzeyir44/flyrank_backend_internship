from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()

class Tasks(BaseModel):
    id: int = Field(..., gt=0)
    title: str = Field(..., min_length=1)
    done: bool = False

class Post_Task(BaseModel):
    title: str = Field(..., min_length=1)

class Update_Tasks(BaseModel):
    id: int | None = Field(None, gt=0)
    title: str | None = Field(None, min_length=1)
    done: bool | None = None

tasks_db: list[dict] = [
    {
        "id": 1,
        "title": "Learn CRUD operation",
        "done": True
    },
    
    { 
        "id": 2,
        "title": "Learn Competitive Programming",
        "done": False
    },
    
    {
        "id": 3,
        "title": "Create the architecture of the application",
        "done": False
    }
]

@app.get('/')
def root():
    return { 
            "name": "Task API", 
            "version": "1.0", 
            "endpoints": ["/tasks"] 
    }

@app.get('/health')
def get_health():
    return {"status": "ok"}

@app.get('/tasks', response_model=list[dict], status_code=status.HTTP_200_OK)
def get_tasks():
    return tasks_db

@app.get('/tasks/{id}', response_model=Tasks, status_code=status.HTTP_200_OK)
def get_by_id(id: int):
    for task in tasks_db:
        if task['id'] == id:
            return task
    
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Task with id {id} not found"
    )

@app.post('/tasks', response_model=Tasks, status_code=status.HTTP_201_CREATED)
def create_task(task: Post_Task):
    new_task = {
        "id": len(tasks_db) + 1,
        "title": task.title,
        "done": False
    }
    
    tasks_db.append(new_task)
    return new_task

@app.patch('/tasks/{id}', response_model=Tasks, status_code=status.HTTP_200_OK)
def update_task(id: int, new_data: Update_Tasks):
    for task in tasks_db:
        if task['id'] == id:
            new_task = new_data.model_dump(exclude_unset=True)
            task.update(new_task)
            return task
    
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = f"Cannot update. Task with id {id} is not found"
    )

@app.delete('/tasks/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int):
    for index, task in enumerate(tasks_db):
        if task['id'] == id:
            tasks_db.pop(index)
            return
    
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = f"Cannot delete. Task with id {id} is not found"
    )