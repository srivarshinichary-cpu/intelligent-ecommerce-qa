import requests


def test_get_product():

    url = "https://dummyjson.com/products/1"

    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert "title" in data
    assert "price" in data

    assert data["id"] == 1


def test_get_all_products():

    url = "https://dummyjson.com/products"

    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()

    assert "products" in data
    assert isinstance(data["products"], list)
    assert len(data["products"]) > 0


def test_create_product():

    url = "https://dummyjson.com/products/add"

    payload = {
        "title": "QA Automation Product",
        "price": 99.99,
        "category": "automation"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 201

    data = response.json()

    assert "id" in data
    assert data["title"] == "QA Automation Product"
    assert data["price"] == 99.99


def test_get_invalid_product():

    url = "https://dummyjson.com/products/99999"

    response = requests.get(url)

    assert response.status_code == 404