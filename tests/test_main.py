from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert 'msg' in data
    assert 'ts' in data
    assert data['msg'] == "Hello World"