from app import FinalProject

def test_index():
    client = FinalProject.test_client()
    response = client.get('/')
    assert response.status_code == 200
