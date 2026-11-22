from app import app

def test_home_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Hello from Azure with Python! V2" in response.data
    assert "Кісліцин Артем".encode("utf-8") in response.data
    assert "КН-24/11".encode("utf-8") in response.data
