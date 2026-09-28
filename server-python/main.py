from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False
    createAt: str = datetime.now().isoformat()

app = FastAPI()

db = [
    {
        "id": 1,
        "title": "Hello 1",
        "completed": True,
        "createAt": "2026-09-28T19:55:02.137742"
    },
    {
        "id": 2,
        "title": "Hello 2",
        "completed": False,
        "createAt": "2026-09-28T19:55:02.137742"
    }
]

@app.get("/api/tasks")
def all_tasks(status: str = None):
    if status == "Completed":
        new_db = []
        for item in db:
            if item.completed == True:
                new_db.append(item)
    if status == "Pending":
        new_db = []
        for item in db:
            if item.completed == False:
                new_db.append(item)

    return db if status == None else new_db

@app.get("/api/health")
def health():
    return {"ok": True}
