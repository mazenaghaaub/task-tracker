def test_index_html_serves_frontend(client):
    response = client.get("/index.html")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Task Tracker Kanban" in response.text


def test_root_serves_frontend(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "Task Tracker Kanban" in response.text
