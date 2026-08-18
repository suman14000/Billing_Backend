from sqlalchemy.orm import Session

from app.models.invoice import Invoice

from app.schemas.invoice import (
    InvoiceCreate,
    InvoiceUpdate,
)


def create_invoice(
    db: Session,
    invoice_data: InvoiceCreate
):
    invoice = Invoice(
        customer_id=invoice_data.customer_id,
        invoice_number=invoice_data.invoice_number,
        invoice_date=invoice_data.invoice_date,
        due_date=invoice_data.due_date,
        subtotal=invoice_data.subtotal,
        tax_amount=invoice_data.tax_amount,
        discount_amount=invoice_data.discount_amount,
        total_amount=invoice_data.total_amount,
        invoice_status=invoice_data.invoice_status,
        notes=invoice_data.notes,
    )

    db.add(invoice)
    db.commit()
    db.refresh(invoice)

    return invoice


def get_invoice(
    db: Session,
    invoice_id: int
):
    return (
        db.query(Invoice)
        .filter(
            Invoice.invoice_id == invoice_id
        )
        .first()
    )


def get_invoices(
    db: Session,
    customer_id: int | None = None,
    skip: int = 0,
    limit: int = 100
):
    query = db.query(Invoice)

    if customer_id is not None:
        query = query.filter(
            Invoice.customer_id == customer_id
        )

    return (
        query
        .offset(skip)
        .limit(limit)
        .all()
    )



def update_invoice(
    db: Session,
    invoice_id: int,
    invoice_data: InvoiceUpdate
):
    invoice = get_invoice(
        db,
        invoice_id
    )

    if not invoice:
        return None

    update_data = invoice_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(invoice, field, value)

    db.commit()
    db.refresh(invoice)

    return invoice


def delete_invoice(
    db: Session,
    invoice_id: int
):
    invoice = get_invoice(
        db,
        invoice_id
    )

    if not invoice:
        return None

    db.delete(invoice)
    db.commit()

    return invoice