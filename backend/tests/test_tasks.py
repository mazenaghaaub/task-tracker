from fastapi.testclient import TestClient

from app.main import app
from app.storage import _reset

client = TestClient(app)


def setup_function():
    _reset()


def test_health_check_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200

    body = response.json()
    assert body["status"] == "ok"
    assert "timestamp" in body


def test_create_task_returns_created_task():
    response = client.post(
        "/tasks",
        json={
            "title": "  Write tests  ",
            "description": "Cover the create endpoint",
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
