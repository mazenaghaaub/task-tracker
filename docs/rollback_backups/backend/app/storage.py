from datetime import date, datetime, timezone
from typing import Optional
from uuid import uuid4

from app.models import TaskCreate, TaskPriority, TaskResponse, TaskStatus, TaskUpdate

_tasks: dict[str, TaskResponse] = {}


def _is_overdue(due_date: Optional[date]) -> bool:
    if due_date is None:
        return False
    return due_date < date.today()


def _serialize_task(task: TaskResponse) -> TaskResponse:
    return task.model_copy(update={"is_overdue": _is_overdue(task.due_date)})


def add_task(payload: TaskCreate) -> TaskResponse:
    now = datetime.now(timezone.utc)
    task_id = str(uuid4())
    task = TaskResponse(
        id=task_id,
        title=payload.title,
        description=payload.description or "",
        status=payload.status,
        priority=payload.priority,
        assignee=payload.assignee,
        due_date=payload.due_date,
        is_overdue=_is_overdue(payload.due_date),
        created_at=now,
        updated_at=now,
    )
    _tasks[task_id] = task
    return task


def get_all_tasks(
    status: Optional[TaskStatus] = None,
    priority: Optional[TaskPriority] = None,
    overdue: Optional[bool] = None,
    search: Optional[str] = None,
) -> list[TaskResponse]:
    tasks = list(_tasks.values())

    if search is not None:
        search_term = search.strip().lower()
        if search_term:
            tasks = [
                t
                for t in tasks
                if search_term in (t.title or "").lower()
                or search_term in (t.description or "").lower()
            ]

    if status is not None:
        tasks = [t for t in tasks if t.status == status]
    if priority is not None:
        tasks = [t for t in tasks if t.priority == priority]
    if overdue is not None:
        tasks = [t for t in tasks if _is_overdue(t.due_date) is overdue]
    return [_serialize_task(task) for task in tasks]


def get_task_by_id(task_id: str) -> Optional[TaskResponse]:
    task = _tasks.get(task_id)
    if task is None:
        return None
    return _serialize_task(task)


def update_task(task_id: str, payload: TaskUpdate) -> Optional[TaskResponse]:
    task = _tasks.get(task_id)
    if task is None:
        return None

    updates = payload.model_dump(exclude_unset=True)
    if not updates:
        return _serialize_task(task)

    updated = task.model_copy(
        update={
            **updates,
            "updated_at": datetime.now(timezone.utc),
        }
    )
    updated = updated.model_copy(update={"is_overdue": _is_overdue(updated.due_date)})
    _tasks[task_id] = updated
    return updated


def delete_task(task_id: str) -> bool:
    if task_id not in _tasks:
        return False
    del _tasks[task_id]
    return True


def _reset() -> None:
    _tasks.clear()
