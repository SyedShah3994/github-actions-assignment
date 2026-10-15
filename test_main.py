from fastapi.testclient import TestClient
from main import add, app

client = TestClient(app)


def test_add():
    assert add(2, 3) == 5


def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello from GitHub Actions!'}


def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}


def test_add_endpoint():
    response = client.get('/add', params={'a': 4, 'b': 6})
    assert response.json() == {'result': 10}