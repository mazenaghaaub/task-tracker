# Verification

## Feature 1 
## Test command
```bash
cd 'C:\Personal\Courses\AI Coding\task-tracker\backend' ; & '..\.venv\Scripts\python.exe' -m pytest tests/test_tasks.py -q
```

## Result
- 24 passed in 0.36s


## Break test
## made due_date required without changing  test_tasks.py
6 failed, 13 passed, 5 errors in 0.37s
FAILED tests/test_tasks.py::test_create_task_valid_returns_201_with_full_body - assert 422 == 201
FAILED tests/test_tasks.py::test_patch_updates_due_date_and_overdue_status - KeyError: 'id'

## Browser Check
1. Due date appears
2. Due date optional in create task
3. No regression in other tasks
4. Overdue filter works

## Feature 2
## Test command
```bash
cd 'C:\Personal\Courses\AI Coding\task-tracker\backend' ; & '..\.venv\Scripts\python.exe' -m pytest tests/test_tasks.py -q
```

## Result
- 28 passed in 0.87s

## Break test
## Added addtional acceptable task status "Urgent" without changing test_tasks.py
python -m pytest -q tests/test_tasks.py
........F...............              [100%]
================= FAILURES =================
_ test_create_task_invalid_priority_returns_422 _

client = <starlette.testclient.TestClient object at 0x0000014DCC80B950>

    def test_create_task_invalid_priority_returns_422(client):
        response = client.post("/tasks", json={"title": "Task", "priority": "Urgent"})
>       assert response.status_code == 422
E       assert 201 == 422
E        +  where 201 = <Response [201 Created]>.status_code

tests\test_tasks.py:95: AssertionError
========= short test summary info ==========
FAILED tests/test_tasks.py::test_create_task_invalid_priority_returns_422 - assert 201 ==422
1 failed, 23 passed in 0.41s
(.venv) PS C:\Personal\Courses\AI Coding\task-tracker\backend> 

## Browser Check
1. All filters appear
2. search by title or description works
3. fitler by priority or status works
4. Combined filters work


## Refactor

### Behavior contract before changing New Task to accept only ToDo Status

| ID | Behavior | How to check manually | Pass/Fail notes |
|---|---|---|---|
| 1 | Board loads tasks into three status columns: To Do, In Progress, Done. | Start backend/frontend, open the board, confirm tasks appear under the column matching their `status`. | Pass if each task appears in exactly one matching column. |
| 2 | Tasks are sorted by priority within each column. | Create or inspect tasks with `High`, `Medium`, and `Low` priority in the same column. | Pass if `High` appears before `Medium`, and `Medium` before `Low`. |
| 3 | Empty board state is shown when there are no tasks. | Clear/reset task data, then reload the board. | Pass if the board shows an empty-state message and the columns remain visible. |
| 4 | Error state is shown when tasks cannot be loaded. | Stop the backend or force `/tasks` to fail, then reload the board. | Pass if an error message appears with retry behavior and the page does not crash. |
| 5 | New Task modal creates a task. | Click `New Task`, fill title and optional fields, save. | Pass if the modal closes and the new task appears after refresh. |
| 6 | Edit modal updates an existing task. | Click `Edit` on a task, change fields, save. | Pass if the modal closes and the updated task appears in the correct column. |
| 7 | Drag-and-drop status update rolls back on server rejection. | Drag a task to an invalid status transition, such as `ToDo` directly to `Done` if backend rejects it. | Pass if the card returns to its original column and an error message is shown. |
| 8 | Search and filters preserve board layout. | Search by title/description, apply status/priority/overdue filters, then clear them. | Pass if only matching tasks show while filters are active, no-match state is visible, and all three columns remain visible. |

### Behavior contract after changing New Task to accept only ToDo Status

| ID | Behavior | How to check manually | Pass/Fail notes |
|---|---|---|---|
| 1 | Board loads tasks into three status columns: To Do, In Progress, Done. | Start backend/frontend, open the board, confirm tasks appear under the column matching their `status`. | Pass if each task appears in exactly one matching column. |
| 2 | Tasks are sorted by priority within each column. | Create or inspect tasks with `High`, `Medium`, and `Low` priority in the same column. | Pass if `High` appears before `Medium`, and `Medium` before `Low`. |
| 3 | Empty board state is shown when there are no tasks. | Clear/reset task data, then reload the board. | Pass if the board shows an empty-state message and the columns remain visible. |
| 4 | Error state is shown when tasks cannot be loaded. | Stop the backend or force `/tasks` to fail, then reload the board. | Pass if an error message appears with retry behavior and the page does not crash. |
| 5 | New Task modal creates a task. | Click `New Task`, fill title and optional fields, save. | Pass if the modal closes and the new task appears after refresh. |
| 6 | New tasks always start in To Do. | Open `New Task` and inspect the status field, then create a task. | Pass if status is fixed/disabled as `ToDo` and the created task appears in the To Do column. |
| 7 | Edit modal updates an existing task. | Click `Edit` on a task, change fields, save. | Pass if the modal closes and the updated task appears in the correct column. |
| 8 | Edit modal still allows status changes for existing tasks. | Open an existing task, change its status where allowed, and save. | Pass if the status field is enabled in edit mode and valid status changes are saved. |
| 9 | Drag-and-drop status update rolls back on server rejection. | Drag a task to an invalid status transition, such as `ToDo` directly to `Done` if backend rejects it. | Pass if the card returns to its original column and an error message is shown. |
| 10 | Search and filters preserve board layout. | Search by title/description, apply status/priority/overdue filters, then clear them. | Pass if only matching tasks show while filters are active, no-match state is visible, and all three columns remain visible. |

