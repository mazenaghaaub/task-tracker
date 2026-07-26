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


## verification of user stories 
1. Coplit added a 5th story
 "As a **team member**, I want task cards to display due date and overdue information so that I can understand task urgency at a glance"

2. Ran the following prompt on Codex 
"
You are a senior developer reviewing requirements before implementation. 
Context: Check the generated user stories for adding due_date with due_date filter feature. Review the user stories in @user-stories.md for testability and scope alignment. Check each story for: - Is the story in scope? - Are the acceptance criteria specific and testable? - Is there at least one meaningful edge case or failure case across the set? - Are any words too vague, such as "works", "properly", or "as expected"? - Did the AI assume a feature that was not requested? Constraints: - Do not generate a new story set. - Suggest minimal edits only."

3.Codex suggested the 5th story was redundant and overlapped with story 4. I checked both and agreed as the filter in Story 4 provides the same functionality so I removed the 5th story.