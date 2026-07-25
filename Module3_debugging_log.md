# Module 3 Debugging Log and Reflection

## Debugging Log
1. What I intentionally broke or what failed: I focused on the task status-transition behavior in the API, where a status change had to be validated rather than accepted blindly.
2. Failing test name and one-line failure summary: test_patch_invalid_transition_todo_to_done_returns_422 — it verifies that an invalid transition is rejected with a 422 response and a helpful detail message.
3. AI assistant's root-cause diagnosis: The issue was in the business-rule layer for status transitions, where the validator needed to enforce the allowed transition map instead of allowing any status update.
4. Whether I accepted or rejected the fix, and why: I accepted the fix because it matched the expectations in [backend/tests/test_tasks.py](backend/tests/test_tasks.py) and the task model's rules for valid transitions.

## Reflection
The VS Code AI assistant helped during my frontend work by suggesting ways to structure the task UI, troubleshoot the interaction between the page and the API, and keep changes small and testable. One place I had to correct or constrain the assistant was when it suggested a larger refactor than the task required, so I kept the work focused on the specific frontend behavior I was trying to support. Inspecting diffs, browser behavior, and pytest output changed the result because they helped me confirm whether the page and the backend were actually matching the expected workflow. One habit I will reuse in later modules is to verify each frontend change against the actual behavior in the app before I accept it.
