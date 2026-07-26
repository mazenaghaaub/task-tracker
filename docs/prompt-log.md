# Prompt Log

# Feature 1 Due Dates

 # A. Prompt 1: User Stories
=> Weak:
    I need to add the following feature to my task tracker project: due dates + overdue filter
    Generate 4 user stories

=> Better
    I need to add the following feature to my task tracker project: due dates + overdue filter 
    Add due date to the modal. Due date is optional. Show due date or overdue pill on cards. Add an overdue filter.
    Test for Valid due date, invalid date format, overdue detection, update due date, filter returns only overdue tasks.
    Generate 5 user stories following the below examples:
    <<
    | US-01 | As a **team member**, I want to create a task so that I can track work that needs to be completed.                                 | 1. A task can be created only when `title` is non-empty after trimming leading and trailing whitespace.<br>2. If `title` is empty or contains only whitespace, the API returns HTTP `422` with the detail message `"Title is required and cannot be blank"`.<br>3. `status` must be exactly one of `ToDo`, `InProgress`, or `Done`, and `priority` must be exactly one of `Low`, `Medium`, or `High`.                       | The system uses one shared task list.                                                  |
    | US-05 | As a **team member**, I want to update a task so that its details remain accurate as work changes.                                 | 1. An existing task can be updated when all provided values satisfy the task validation rules.<br>2. If the updated `title` is empty or whitespace-only after trimming, the API returns HTTP `422` with the detail message `"Title is required and cannot be blank"`.<br>3. An update with a status outside `ToDo`, `InProgress`, or `Done`, or a priority outside `Low`, `Medium`, or `High`, is rejected with HTTP `422`. | Updates may use `PUT` or `PATCH`; the project should choose one approach consistently.   
    >>
    Constraints: 
    Do not touch the code or implement any changes
    - Use "team member" as the user role. - Do not mention login, authentication, user accounts, admin roles, notifications, mobile, or real-time updates. - Include at least one failure case across the generated stories. 
    Output format: Return each story with Story and Acceptance Criteria headings.
    Save the user stories to user-stories.md

    Prompt Summary
    AI returned list of user stories. I verified the stories against requirements using another tool, reviewed them myself, then applied the changes that made sense.


# B. Prompt 2: ADR
    ==> You are a senior full-stack developer helping me evaluate implementation options for the due date feature.
    Context: I am adding due date feauture for the task-tracker
    Requirements: check user stories in @user-stories.md
    Task: Propose two different implementation options

    For each option, provide: 1. Features 2. Changes to frontend and backend 3.Validations and how to implement them 4. Files to be changed
    Return Option A and Option B in clearly separated sections. Do not choose for me.

Prompt Summary: AI gave me 2 implementation options with pros and cons. I reviewed both against requirements and scope and decided to go with option A.

# C. Prompt 3: Implementation
==>You are a senrior backend developer.
Context: I am adding backend support for due date feature. Details in @user-stories.md
Requirements: check Feature 1 in mini-adr.md file
Constraints: Use the existing project architecture and keep the changes minimal
Task: Show me a summary of the changes you will make in each file with explanation
Do not write any code yet

==>You are a senior front end developer.
Context: I am adding front-end support for due date feature
Requirements: check Feature 1 in mini-adr.md file
Constraints: Use the existing project architecture and keep the changes minimal
Task: Show me a summary of the changes you will make in each file with explanation
Do not write any code yet

Prompt Summary: AI gave me implementation plan and proposed changes to specific files. I reviewed the plan against requirements and accepted the code changes


## Feature 2 : Search and Combined filter
# A. Prompt 1 : 
==> Weak
I need to add the following feature to my task tracker project: Search + Combined filters
Generate 4 user stories

==> Better
I need to add the following feature to my task tracker project: Search + combined filters
Add a compact filter/search bar above the board. Keep columns visible and preserve empty states.

Test Search title/description, combine status + priority. No matches returns 200 with [], invalid filter value returns 422 if backend validates it.
Generate 5 user stories following the below examples:
<<
 | US-01 | As a **team member**, I want to create a task so that I can track work that needs to be completed.                                 | 1. A task can be created only when `title` is non-empty after trimming leading and trailing whitespace.<br>2. If `title` is empty or contains only whitespace, the API returns HTTP `422` with the detail message `"Title is required and cannot be blank"`.<br>3. `status` must be exactly one of `ToDo`, `InProgress`, or `Done`, and `priority` must be exactly one of `Low`, `Medium`, or `High`.                       | The system uses one shared task list.                                                  |
 | US-05 | As a **team member**, I want to update a task so that its details remain accurate as work changes.                                 | 1. An existing task can be updated when all provided values satisfy the task validation rules.<br>2. If the updated `title` is empty or whitespace-only after trimming, the API returns HTTP `422` with the detail message `"Title is required and cannot be blank"`.<br>3. An update with a status outside `ToDo`, `InProgress`, or `Done`, or a priority outside `Low`, `Medium`, or `High`, is rejected with HTTP `422`. | Updates may use `PUT` or `PATCH`; the project should choose one approach consistently. |
>>
Constraints: 
Do not touch the code or implement any changes
- Use "team member" as the user role. - Do not mention login, authentication, user accounts, admin roles, notifications, mobile, or real-time updates. - Include at least one failure case across the generated stories. 
Output format: Return each story with Story and Acceptance Criteria headings.
Save the user stories to docs/user-stories.md under Feature 2

Prompt Summary
AI returned list of user stories. I verified the stories against requirements using another tool, reviewed them myself, then made minor changes.




# B. Prompt 2: ADR
==> You are a senior full-stack developer helping me evaluate implementation options for the due date feature.
Context: I am adding search and combined filter feauture for the task-tracker
Requirements: check user stories in @file:user-stories.md (feature 2)
Task: Propose two different implementation options
For each option, provide: 1. Features 2. Changes to frontend and backend 3.Validations and how to implement them 4. Files to be changed 5. Pros and Cons of each option
Return Option A and Option B in clearly separated sections. Do not choose for me.

- Prompt Summary: AI gave me 2 implementation options with pros and cons. I reviewed both against requirements and scope and decided to go with option A.

C. Prompt 3: Implementation
==>I am a a senrio backend developer.
Context: I am adding backend support for search and combined filter feature. Details in Feature 2 in user-stories.md
Requirements: check Feature 2 in mini-adr.md file
Constraints: Use the existing project architecture and keep the changes minimal
Task: Show me a summary of the changes you will make in each file with explanation
Do not write any code yet

==> You are a senrior front end developer.
Context: I am adding front-end support for feature search and combined filter. Details in @user-stories.md under Feature 2
Requirements: check Feature 2 in mini-adr.md file
Constraints: Use the existing project architecture and keep the changes minimal
Task: Show me a summary of the changes you will make in each file with explanation
Do not write any code yet

Prompt Summary: AI gave me implementation plan and proposed changes to specific files. I reviewed the plan against requirements and accepted the code changes