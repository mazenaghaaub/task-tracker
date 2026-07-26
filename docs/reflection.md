I used both Copilot and Codex through out this excercise. I followed the following strategy: Plan on one tool and verify on the other. Examples:
(a) Generate user stories on copilot. Verify against requirements on Codex.
(b) Generate ADR on Copilot. Implement on Codex. 

The biggest help was the file-reading and editing workflow, which let me inspect the existing FastAPI models, storage layer, and tests in [backend/app/models.py](../backend/app/models.py), [backend/app/storage.py](../backend/app/storage.py), and [backend/tests/test_tasks.py](../backend/tests/test_tasks.py) without manually tracing the whole codebase. I also used the terminal-based test runner to validate behavior end to end, which was especially useful because it gave me concrete evidence when the new due-date logic was correct or still failing. That feedback loop was faster than guessing.

One moment where AI helped a lot was when I was adding the backend support for due dates. The assistant quickly identified the right places to extend the request/response models, update the in-memory storage logic, and add test cases for invalid dates, overdue detection, and overdue filtering. That saved time and kept the work focused.

One moment where AI slowed me down was when the initial implementation assumptions were too broad. For example, I had to correct course several times around whether due dates should be optional or required, and whether the overdue logic should live in the API, storage layer, or both. The model was fast to propose changes, but it also needed careful review to keep the scope aligned with the stories and avoid overbuilding.

A clear place where review changed the result was the test-driven iteration around overdue behavior. After I reviewed the failing tests and compared them to the user stories, I refined the implementation so the backend handled the due-date field, validation, and filtering in a way that matched the expected API behavior rather than just making the code “look” correct. That review step was what turned a speculative implementation into a reliable one.
