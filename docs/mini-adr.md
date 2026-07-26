# Mini ADR — Option A: Minimal, Incremental Feature 1: Due Date

## Status
Proposed
## Context
The task tracker needs to support due dates and overdue visibility for the current user stories in [user-stories.md](../user-stories.md). The feature must be added without introducing unnecessary architectural complexity, and it should fit the current simple backend/frontend structure.

## Decision
Implement the due date feature in a minimal, incremental way:
- Add an optional due date field to task create/update payloads.
- Store and return the value through the existing API flow.
- Show the due date or an overdue badge on task cards.
- Add a simple overdue-only filter in the UI and API.

## Why this option
This approach matches the current project size and keeps the change focused on the requested behavior. It avoids introducing new abstractions or larger refactors while still supporting the required stories.

## Implementation notes
- Backend changes will be limited to models, task storage, and task endpoints.
- Frontend changes will be limited to the task form/modal and task card rendering.
- Validation will use standard date parsing for the ISO date format YYYY-MM-DD, with clear 422 responses for invalid input.
- Overdue state will be computed from the current date at runtime.

## Consequences
### Positive
- Faster to implement and verify.
- Low risk to existing task behavior.
- Easy to extend later if more due-date behavior is needed.

### Trade-offs
- The overdue logic remains relatively simple.
- The implementation may be less reusable for future calendar-style features.

## Files affected
- [backend/app/models.py](../backend/app/models.py)
- [backend/app/main.py](../backend/app/main.py)
- [backend/app/storage.py](../backend/app/storage.py)
- [frontend/index.html](../frontend/index.html)
- [backend/tests/test_tasks.py](../backend/tests/test_tasks.py)

## Feature 2: Search and Combined Filters

## Status
Proposed
## Context
The task tracker needs a compact search and filter experience above the board so that a team member can quickly narrow the visible tasks by keyword, status, and priority. The feature must fit the project’s current lightweight architecture and support the user stories in [user-stories.md](../user-stories.md) without introducing unnecessary complexity.

## Decision
Implement the search and combined filters using a backend-driven approach:
- Add a compact search input and status/priority filter controls above the board.
- Send the active search and filter values to the backend through query parameters.
- Apply filtering server-side so the API is the single source of truth for visible tasks.
- Preserve the three board columns and show a clear empty state when no tasks match.

## Why this option
This option aligns with the existing FastAPI backend and static frontend structure while keeping the filtering rules testable and consistent. It also ensures that the same filtering logic is used for the board view and for future API consumers.

## Implementation notes
- Frontend changes will add a compact toolbar above the board with a search input and dropdown filters.
- Backend changes will extend the task list endpoint to accept `search`, `status`, and `priority` query parameters.
- Filtering will use case-insensitive text matching against title and description, combined with AND logic across all active filters.
- Invalid status or priority values will be rejected with HTTP 422 by the backend validation layer.
- When no tasks match, the API should return HTTP 200 with an empty list and the UI should render the empty state without hiding the columns.

## Consequences
### Positive
- Filtering behavior is centralized and easier to test.
- The backend and frontend stay aligned around the same rules.
- The design is easy to extend later for additional filter types.

### Trade-offs
- The UI depends on a backend round-trip for every filter change.
- More backend code is required than a purely client-side filter implementation.

## Files affected
- [frontend/index.html](../frontend/index.html)
- [backend/app/main.py](../backend/app/main.py)
- [backend/app/storage.py](../backend/app/storage.py)
- [backend/app/models.py](../backend/app/models.py)
- [backend/tests/test_tasks.py](../backend/tests/test_tasks.py)

## Decision note
AI suggested two implementation paths for the search and combined filter feature. Option A keeps filtering on the backend so the API is the single source of truth, while Option B moves the filtering logic into the frontend and keeps the backend simpler. I chose Option A because it matches the current FastAPI-based architecture, makes the behavior easier to test, and aligns with the user stories for validation and empty-state handling. I rejected the frontend-only approach as too complex for this stage because it pushes more business logic into the UI and makes the behavior harder to validate consistently across the app. In particular, the parts of Option B that were out of scope for this iteration were: adding a full client-side state management layer for task filtering, introducing extra UI-only abstractions for query state, and building a richer frontend-only validation and error-handling experience that is not required by the current stories.

