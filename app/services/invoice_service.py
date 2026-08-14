from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.crud import invoice as invoice_crud
from app.models.invoice import Invoice
from app.schemas.invoice import InvoiceCreate, InvoiceUpdate


def create_invoice(
    db: Session,
    invoice_data: InvoiceCreate
):
    existing_invoice = (
        db.query(Invoice)
        .filter(
            Invoice.invoice_number
            == invoice_data.invoice_number
        )
        .first()
    )

    if existing_invoice:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invoice number already exists"
        )

    return invoice_crud.create_invoice(
        db,
        invoice_data
    )


def get_invoice(
    db: Session,
    invoice_id: int
):
    existing_invoice = invoice_crud.get_invoice(
        db,
        invoice_id
    )

    if not existing_invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice not found"
        )

    return existing_invoice


def get_invoices(
    db: Session
):
    return invoice_crud.get_invoices(db)


def update_invoice(
    db: Session,
    invoice_id: int,
    invoice_data: InvoiceUpdate
):
    existing_invoice = invoice_crud.get_invoice(
        db,
        invoice_id
    )

    if not existing_invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice not found"
        )

    return invoice_crud.update_invoice(
        db,
        invoice_id,
        invoice_data
    )


def delete_invoice(
    db: Session,
    invoice_id: int
):
    existing_invoice = invoice_crud.get_invoice(
        db,
        invoice_id
    )

    if not existing_invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice not found"
        )

    return invoice_crud.delete_invoice(
        db,
        invoice_id
    )