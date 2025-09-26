from fastapi.testclient import TestClient

from app.main import app


def test_me_returns_stub_user():
    client = TestClient(app)
    r = client.get("/me")
    assert r.status_code == 200
    data = r.json()
    assert data["org_id"] == 1
    assert data["role"] in ("Admin", "Manager", "Staff")
