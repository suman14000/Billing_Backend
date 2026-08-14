from sqlalchemy.orm import Session

from app.models.invoice import Invoice
from app.schemas.invoice import InvoiceCreate, InvoiceUpdate


def create_invoice(
    db: Session,
    invoice_data: InvoiceCreate
):
    new_invoice = Invoice(
        billing_id=invoice_data.billing_id,
        invoice_number=invoice_data.invoice_number,
        invoice_date=invoice_data.invoice_date,
        due_date=invoice_data.due_date,
        total_amount=invoice_data.total_amount,
        status=invoice_data.status
    )

    db.add(new_invoice)
    db.commit()
    db.refresh(new_invoice)

    return new_invoice


def get_invoice(
    db: Session,
    invoice_id: int
):
    return (
        db.query(Invoice)
        .filter(Invoice.id == invoice_id)
        .first()
    )


def get_invoices(
    db: Session
):
    return db.query(Invoice).all()


def update_invoice(
    db: Session,
    invoice_id: int,
    invoice_data: InvoiceUpdate
):
    existing_invoice = (
        db.query(Invoice)
        .filter(Invoice.id == invoice_id)
        .first()
    )

    if not existing_invoice:
        return None

    update_data = invoice_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(existing_invoice, field, value)

    db.commit()
    db.refresh(existing_invoice)

    return existing_invoice


def delete_invoice(
    db: Session,
    invoice_id: int
):
    existing_invoice = (
        db.query(Invoice)
        .filter(Invoice.id == invoice_id)
        .first()
    )

    if not existing_invoice:
        return None

    db.delete(existing_invoice)
    db.commit()

    return existing_invoice