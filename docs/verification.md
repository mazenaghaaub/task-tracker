# Verification

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
