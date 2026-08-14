from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.invoice import (
    InvoiceCreate,
    InvoiceResponse,
    InvoiceUpdate
)
from app.services import invoice_service


router = APIRouter(
    prefix="/invoices",
    tags=["Invoices"]
)


@router.post(
    "/",
    response_model=InvoiceResponse,
    status_code=status.HTTP_201_CREATED
)
def create_invoice(
    invoice_data: InvoiceCreate,
    db: Session = Depends(get_db)
):
    return invoice_service.create_invoice(
        db,
        invoice_data
    )


@router.get(
    "/",
    response_model=list[InvoiceResponse]
)
def get_invoices(
    db: Session = Depends(get_db)
):
    return invoice_service.get_invoices(db)


@router.get(
    "/{invoice_id}",
    response_model=InvoiceResponse
)
def get_invoice(
    invoice_id: int,
    db: Session = Depends(get_db)
):
    return invoice_service.get_invoice(
        db,
        invoice_id
    )


@router.put(
    "/{invoice_id}",
    response_model=InvoiceResponse
)
def update_invoice(
    invoice_id: int,
    invoice_data: InvoiceUpdate,
    db: Session = Depends(get_db)
):
    return invoice_service.update_invoice(
        db,
        invoice_id,
        invoice_data
    )


@router.delete(
    "/{invoice_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_invoice(
    invoice_id: int,
    db: Session = Depends(get_db)
):
    invoice_service.delete_invoice(
        db,
        invoice_id
    )

    return None