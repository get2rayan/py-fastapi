import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import storage
from app.main import app


@pytest.fixture(autouse=True)
def clear_items():
    storage.items.clear()
    yield
    storage.items.clear()


@pytest.fixture
def client():
    return TestClient(app)


def test_root_route(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Store API Service!"}


def test_create_item_and_list_by_category(client):
    item_payload = {
        "name": "Apple",
        "price": 2.5,
        "quantity": 3,
        "category": "produce",
    }

    create_response = client.post("/item/", json=item_payload)
    assert create_response.status_code == 200
    created = create_response.json()
    assert created["name"] == "Apple"
    assert created["id"] == 1

    list_response = client.get("/items?category=produce")
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1
    assert list_response.json()[0]["name"] == "Apple"


def test_get_missing_item_returns_404(client):
    response = client.get("/items/banana")

    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


def test_delete_and_update_item(client):
    create_response = client.post(
        "/item/",
        json={
            "name": "Orange",
            "price": 3.0,
            "quantity": 5,
            "category": "produce",
        },
    )
    item_id = create_response.json()["id"]

    delete_response = client.delete(f"/items/{create_response.json()['name']}")
    assert delete_response.status_code == 200
    assert delete_response.json()["name"] == "Orange"

    update_response = client.put(
        f"/items/{item_id}",
        json={"price": 4.5, "quantity": 8},
    )
    assert update_response.status_code == 404
    assert update_response.json() == {"detail": "Item not found"}

    second_create = client.post(
        "/item/",
        json={
            "name": "Mango",
            "price": 2.0,
            "quantity": 1,
            "category": "fruit",
        },
    )
    item_id = second_create.json()["id"]

    update_response = client.put(
        f"/items/{item_id}",
        json={"price": 4.5, "quantity": 8},
    )
    assert update_response.status_code == 200
    assert update_response.json()["price"] == 4.5
    assert update_response.json()["quantity"] == 8
