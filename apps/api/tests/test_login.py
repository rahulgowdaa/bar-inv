from fastapi.testclient import TestClient

from app.main import app


def test_login_stub():
    client = TestClient(app)
    r = client.post("/auth/login", json={"email": "a@b.c", "password": "x"})
    assert r.status_code == 200
    assert r.json()["access_token"] == "stub"
