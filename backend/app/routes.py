from fastapi import APIRouter, status

from app.models import TaskCreate, TaskResponse
from app.storage import add_task

router = APIRouter()


@router.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate) -> TaskResponse:
    return add_task(payload)
