# User Stories

## Feature 1: Due Date

## Story 1
**Story**  
As a **team member**, I want to create a task with an optional due date so that I can track when work is expected to be completed.

**Acceptance Criteria**  
1. A task can be created with a valid due date in the expected date format.  
2. A task can be created without providing a due date.  
3. If the due date is provided in an invalid format, the API returns HTTP 422 with a clear validation error.  
4. The task is saved with the submitted due date when the input is valid.

## Story 2
**Story**  
As a **team member**, I want to update a task’s due date so that the task remains accurate as priorities change.

**Acceptance Criteria**  
1. An existing task can be updated with a new valid due date.  
2. An existing task can be updated to remove its due date when the field is cleared.  
3. If an invalid due date format is provided during update, the API returns HTTP 422.  
4. The updated due date is reflected on the task after a successful update.

## Story 3
**Story**  
As a **team member**, I want to see whether a task is overdue so that I can focus on work that is past due.

**Acceptance Criteria**  
1. A task is marked overdue when its due date is earlier than the current date.  
2. A task is not marked overdue when its due date is today or in the future.  
3. A task without a due date is not shown as overdue.  
4. Overdue status is visible on the task card so it can be identified quickly.

## Story 4
**Story**  
As a **team member**, I want to filter tasks to show only overdue items so that I can review urgent work efficiently.

**Acceptance Criteria**  
1. A filter option allows the user to view only overdue tasks.  
2. When the overdue filter is applied, only tasks with overdue status are returned.  
3. Tasks that are not overdue are excluded from the filtered result.  
4. Clearing the overdue filter returns the full task list.


## Verification of user stories 
1. Coplit added a 5th story that looked close to Story 4
 "As a **team member**, I want task cards to display due date and overdue information so that I can understand task urgency at a glance"

2. Ran the following prompt on Codex 
"
You are a senior developer reviewing requirements before implementation. 
Context: Check the generated user stories for adding due_date with due_date filter feature. Review the user stories in @user-stories.md for testability and scope alignment. Check each story for: - Is the story in scope? - Are the acceptance criteria specific and testable? - Is there at least one meaningful edge case or failure case across the set? - Are any words too vague, such as "works", "properly", or "as expected"? - Did the AI assume a feature that was not requested? Constraints: - Do not generate a new story set. - Suggest minimal edits only."

3.Codex suggested the 5th story was redundant and overlapped with story 4. I checked both and agreed as the filter in Story 4 provides the same functionality and similar acceptance criteria so I removed the 5th story.


## Feature 2: Search + Combined Filters

## Story 1
**Story**  
As a **team member**, I want to search tasks by title or description so that I can quickly find tasks related to a topic or keyword.

**Acceptance Criteria**  
1. A user can enter a search term and submit it to filter the task list.  
2. Tasks whose title or description contains the search term (case-insensitive) are included in the results.  
3. Tasks whose title or description do not contain the search term are excluded from the results.  
4. An empty or cleared search restores the full task list.

## Story 2
**Story**  
As a **team member**, I want to filter tasks by status so that I can focus on tasks that need attention.

**Acceptance Criteria**  
1. A user can select a single status filter such as ToDo, InProgress, or Done.  
2. Only tasks matching the selected status are returned when the filter is applied.  
3. Tasks with other statuses are excluded from the filtered result.  
4. An invalid status filter value is rejected with HTTP 422 when backend validation is enabled.

## Story 3
**Story**  
As a **team member**, I want to filter tasks by priority so that I can focus on the most urgent work.

**Acceptance Criteria**  
1. A user can select a single priority filter such as Low, Medium, or High.  
2. Only tasks matching the selected priority are returned when the filter is applied.  
3. Tasks with other priorities are excluded from the filtered result.  
4. An invalid priority filter value is rejected with HTTP 422 when backend validation is enabled.

## Story 4
**Story**  
As a **team member**, I want to combine search text with status and priority filters so that I can narrow the board to the exact tasks I need.

**Acceptance Criteria**  
1. When search and one or more filters are active, only tasks that match all active criteria are returned.  
2. A task that matches the search text but not the selected status or priority is excluded from the result.  
3. A task that matches the selected status or priority but not the search text is excluded from the result.  
4. No matches for the active combination returns HTTP 200 with an empty list.

## Story 5
**Story**  
As a **team member**, I want the filter and search controls to preserve the board layout and empty states so that the interface remains clear when no tasks match.

**Acceptance Criteria**  
1. A compact filter and search bar is displayed above the board without hiding the task columns.  
2. The board columns remain visible when filters are applied and when no tasks match.  
3. An empty state is shown clearly when the current search and filter combination returns no tasks.  


## Story 6
**Story**  
As a **team member**, I want clearing search terms or removing filters to restore the matching board view so that I can easily return to my broader task list.

**Acceptance Criteria**  
1. When the search term is cleared, tasks that match the remaining active filters are shown again.  
2. When a status filter is removed, tasks that match the remaining search term and priority filter are shown again.  
3. When a priority filter is removed, tasks that match the remaining search term and status filter are shown again.  
4. When all search terms and filters are cleared, the full task list is shown across the three board columns.  
5. The three board columns remain visible after any search or filter is cleared.

## Verification of user stories 
1. Copilot generated 5 stories
2. Validated on Codex with the following prompt
You are a senior developer reviewing requirements before implementation.
Context: Check the generated user stories for search filter feature. <<requirements>> Review the user stories in [user-stories.md](docs/user-stories.md) for testability and scope alignment. Check each story for: - Is the story in scope? - Are the acceptance criteria specific and testable? - Is there at least one meaningful edge case or failure case across the set? - Are any words too vague, such as "works", "properly", or "as expected"? - Did the AI assume a feature that was not requested? Constraints: - Do not generate a new story set. - Suggest minimal edits only
3. Codex suggested to add 1 acceptance criteria to Story 5 related to reset. I realized clearing filters deserves a full story.
4. Asked Codex to add a 6th story to reset when clearing filter status:
"Create a new story to cover "After the search term is cleared or filters are removed, the three board columns remain visible and matching tasks are shown again"
