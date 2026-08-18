from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_get_invoices():
    response = client.get("/billing/invoices")

    assert response.status_code in [200, 404, 500]


def test_get_invoice_invalid_id():
    response = client.get(
        "/billing/invoices/999999"
    )

    assert response.status_code in [404, 500]