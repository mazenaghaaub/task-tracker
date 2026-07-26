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
