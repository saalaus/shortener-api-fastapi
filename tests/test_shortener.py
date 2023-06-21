import pytest
from fastapi.testclient import TestClient

from shortener_api.utils.random_slug import generate_slug


def test_my_test(client: TestClient):
    data = {
        "url": "https://www.youtube.com/",
        "name": "vkdotcom55"
    }
    response = client.post("/api/url/new", json=data)
    assert response.status_code == 201
