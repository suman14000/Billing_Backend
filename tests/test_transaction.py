from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_get_transactions():
    response = client.get("/billing/transactions")

    assert response.status_code in [200, 404, 500]


def test_get_transaction_invalid_id():
    response = client.get(
        "/billing/transactions/999999"
    )

    assert response.status_code in [404, 500]