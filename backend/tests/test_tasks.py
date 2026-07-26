def test_create_task_valid_returns_201_with_full_body(client):
    response = client.post(
        "/tasks",
        json={
            "title": "  Write tests  ",
            "description": "Cover the create endpoint",
            "status": "ToDo",
            "priority": "High",
            "assignee": "Maya",
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["id"]
    assert body["title"] == "Write tests"
    assert body["description"] == "Cover the create endpoint"
    assert body["status"] == "ToDo"
    assert body["priority"] == "High"
    assert body["assignee"] == "Maya"
    assert body["created_at"]
    assert body["updated_at"]


from datetime import date, timedelta


def test_create_task_missing_title_returns_422(client):
    response = client.post("/tasks", json={"priority": "High"})
    assert response.status_code == 422


def test_create_task_with_valid_due_date_returns_201_and_preserves_value(client):
    due_date = (date.today() + timedelta(days=3)).strftime("%Y-%m-%d")

    response = client.post("/tasks", json={"title": "Task", "due_date": due_date})

    assert response.status_code == 201
    body = response.json()
    assert body["due_date"] == due_date
    assert body["is_overdue"] is False


def test_create_task_with_invalid_due_date_returns_422(client):
    response = client.post("/tasks", json={"title": "Task", "due_date": "2025/01/01"})

    assert response.status_code == 422


def test_create_task_with_past_due_date_is_marked_overdue(client):
    due_date = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")

    response = client.post("/tasks", json={"title": "Task", "due_date": due_date})

    assert response.status_code == 201
    assert response.json()["is_overdue"] is True


def test_patch_updates_due_date_and_overdue_status(client):
    create_response = client.post("/tasks", json={"title": "Task"})
    task_id = create_response.json()["id"]
    new_due_date = (date.today() + timedelta(days=2)).strftime("%Y-%m-%d")

    response = client.patch(f"/tasks/{task_id}", json={"due_date": new_due_date})

    assert response.status_code == 200
    body = response.json()
    assert body["due_date"] == new_due_date
    assert body["is_overdue"] is False


def test_list_tasks_filter_by_overdue_returns_only_overdue_tasks(client):
    overdue_date = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    future_date = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    client.post("/tasks", json={"title": "Overdue task", "due_date": overdue_date})
    client.post("/tasks", json={"title": "Upcoming task", "due_date": future_date})

    response = client.get("/tasks", params={"overdue": "true"})

    assert response.status_code == 200
    body = response.json()
    assert len(body) == 1
    assert body[0]["title"] == "Overdue task"
    assert body[0]["is_overdue"] is True


def test_create_task_blank_title_returns_422(client):
    response = client.post("/tasks", json={"title": "   "})
    assert response.status_code == 422


def test_create_task_invalid_priority_returns_422(client):
    response = client.post("/tasks", json={"title": "Task", "priority": "Urgent"})
    assert response.status_code == 422


def test_create_task_unknown_field_returns_422(client):
    response = client.post("/tasks", json={"title": "Task", "unknown": "field"})
    assert response.status_code == 422


def test_list_tasks_empty_returns_200_and_empty_list(client):
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == []


def test_list_tasks_filter_by_status_no_match_returns_200_and_empty_list(client):
    client.post("/tasks", json={"title": "Task", "status": "ToDo"})

    response = client.get("/tasks", params={"status": "Done"})

    assert response.status_code == 200
    assert response.json() == []


def test_list_tasks_filter_by_priority_returns_only_matches(client):
    client.post("/tasks", json={"title": "Low task", "priority": "Low"})
    high_response = client.post("/tasks", json={"title": "High task", "priority": "High"})
    high_task = high_response.json()

    response = client.get("/tasks", params={"priority": "High"})

    assert response.status_code == 200
    body = response.json()
    assert len(body) == 1
    assert body[0]["id"] == high_task["id"]
    assert body[0]["priority"] == "High"


def test_get_task_by_id_returns_task(client, created_task):
    response = client.get(f"/tasks/{created_task['id']}")

    assert response.status_code == 200
    assert response.json() == created_task


def test_get_task_by_id_not_found_returns_404_with_detail(client):
    task_id = "missing-task-id"

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 404
    assert response.json() == {"detail": f"Task with id {task_id} not found"}


def test_patch_partial_update_keeps_other_fields(client):
    create_response = client.post(
        "/tasks",
        json={
            "title": "Original title",
            "description": "Original description",
            "priority": "High",
            "assignee": "Maya",
        },
    )
    task = create_response.json()

    response = client.patch(f"/tasks/{task['id']}", json={"title": "Updated title"})

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == task["id"]
    assert body["title"] == "Updated title"
    assert body["description"] == "Original description"
    assert body["status"] == "ToDo"
    assert body["priority"] == "High"
    assert body["assignee"] == "Maya"


def test_patch_not_found_returns_404(client):
    task_id = "missing-task-id"

    response = client.patch(f"/tasks/{task_id}", json={"title": "Updated title"})

    assert response.status_code == 404
    assert response.json() == {"detail": f"Task with id {task_id} not found"}


def test_patch_valid_transition_todo_to_inprogress_returns_200(client, created_task):
    response = client.patch(
        f"/tasks/{created_task['id']}",
        json={"status": "InProgress"},
    )

    assert response.status_code == 200
    assert response.json()["status"] == "InProgress"


def test_patch_invalid_transition_todo_to_done_returns_422(client, created_task):
    response = client.patch(
        f"/tasks/{created_task['id']}",
        json={"status": "Done"},
    )

    assert response.status_code == 422
    assert "Invalid status transition from ToDo to Done" in response.json()["detail"]


def test_patch_same_status_returns_422(client, created_task):
    response = client.patch(
        f"/tasks/{created_task['id']}",
        json={"status": "ToDo"},
    )

    assert response.status_code == 422
    assert "Invalid status transition from ToDo to ToDo" in response.json()["detail"]


def test_patch_valid_transition_inprogress_to_done_returns_200(client):
    create_response = client.post(
        "/tasks",
        json={
            "title": "In progress task",
            "description": "Transition to done",
            "status": "InProgress",
            "priority": "High",
            "assignee": "Maya",
        },
    )
    task = create_response.json()

    response = client.patch(
        f"/tasks/{task['id']}",
        json={"status": "Done"},
    )

    assert response.status_code == 200
    assert response.json()["status"] == "Done"


def test_patch_invalid_transition_done_to_todo_returns_422(client):
    create_response = client.post(
        "/tasks",
        json={
            "title": "Completed task",
            "description": "Transition back to todo",
            "status": "Done",
            "priority": "High",
            "assignee": "Maya",
        },
    )
    task = create_response.json()

    response = client.patch(
        f"/tasks/{task['id']}",
        json={"status": "ToDo"},
    )

    assert response.status_code == 422
    assert "Invalid status transition from Done to ToDo" in response.json()["detail"]


def test_delete_existing_returns_204_no_body(client, created_task):
    response = client.delete(f"/tasks/{created_task['id']}")

    assert response.status_code == 204
    assert response.content == b""


def test_delete_missing_returns_404(client):
    task_id = "missing-task-id"

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 404
    assert response.json() == {"detail": f"Task with id {task_id} not found"}
