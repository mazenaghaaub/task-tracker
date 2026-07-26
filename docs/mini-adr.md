# Mini ADR — Option A: Minimal, Incremental Feature 1: Due Date Support

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
