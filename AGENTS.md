# Repository Guidelines

## Tech Stack

- Python 3.13.14
- FastAPI `0.115.0`
- Pydantic v2 `2.9.2`
- Uvicorn `0.30.6`
- pytest `8.3.3`
- httpx `0.27.2`
- Vanilla JavaScript frontend in `frontend/index.html`

## Run Command

Run from `backend/`:

```powershell
uvicorn app.main:app --reload --port 8000
```

The backend also serves the frontend at `/` and `/index.html`.

## Test Command

Run from `backend/` after activating the project virtual environment:

```powershell
pytest -v
```

If the venv is not active, run from `backend/` with the root venv explicitly:

```powershell
..\.venv\Scripts\python.exe -m pytest -v
```

## Architecture Summary

- `backend/app/main.py` creates the FastAPI app, serves `frontend/index.html`, and defines task read/update/delete endpoints plus `/health`.
- `backend/app/routes.py` defines task creation.
- `backend/app/models.py` defines task request/response models, status values, priority values, and title validation.
- `backend/app/storage.py` stores tasks in memory, applies search/filter behavior, computes overdue state, and updates/deletes tasks.
- `backend/app/business_rules.py` contains task status transition rules.
- `backend/tests/` contains pytest coverage for API behavior and frontend serving.
- `frontend/index.html` contains the vanilla JavaScript Kanban UI.

## Business Rules

- Task status values are exactly `ToDo`, `InProgress`, and `Done`.
- Allowed status transitions are `ToDo -> InProgress`, `InProgress -> Done`, and `Done -> InProgress`.
- Same-status updates are invalid because they are not in `VALID_TRANSITIONS`.
- Any transition not listed above returns HTTP `422`.

## UI States and CORS Notes

- The frontend tracks board states: `loading`, `ready`, `empty`, and `error`.
- Empty UI distinguishes no tasks from no matching tasks when search or filters are active.
- The UI supports search, status filter, priority filter, overdue filter, modal create/edit, and drag-and-drop status updates.
- No `CORSMiddleware` configuration is present in `backend/app/main.py`.
- The frontend uses `API_BASE_URL = "http://localhost:8000"` and is also served by the backend.

## Do-Not Rules

- Do not add authentication without asking.
- Do not add a database without asking.
- Do not add deployment steps without asking.
- Do not make major UI changes without asking.
