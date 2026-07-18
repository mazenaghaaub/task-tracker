from app.schemas import TaskResponse

# In-memory task store, keyed by task id.
tasks: dict[int, TaskResponse] = {}

# Simple application-managed integer id sequence.
next_id: int = 1