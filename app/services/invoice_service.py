from datetime import date
from sqlalchemy.orm import Session

from app.crud.invoice import (
    create_invoice as crud_create_invoice,
    get_invoice,
    update_invoice as crud_update_invoice,
    delete_invoice as crud_delete_invoice,
)

from app.crud.billing import get_customer

from app.schemas.invoice import (
    InvoiceCreate,
    InvoiceUpdate,
)


def create_invoice(
    db: Session,
    invoice_data: InvoiceCreate
):
    # Check customer exists
    customer = get_customer(
        db,
        invoice_data.customer_id
    )

    if not customer:
        raise ValueError(
            "Customer not found"
        )

  
    if invoice_data.invoice_date > date.today():
        raise ValueError(
            "Invoice date cannot be in the future"
        )


    if (
        invoice_data.due_date is not None
        and invoice_data.due_date
        < invoice_data.invoice_date
    ):
        raise ValueError(
            "Due date cannot be before invoice date"
        )

   
    if invoice_data.subtotal < 0:
        raise ValueError(
            "Subtotal cannot be negative"
        )

    if invoice_data.tax_amount < 0:
        raise ValueError(
            "Tax amount cannot be negative"
        )

    if invoice_data.discount_amount < 0:
        raise ValueError(
            "Discount amount cannot be negative"
        )

    if invoice_data.total_amount < 0:
        raise ValueError(
            "Total amount cannot be negative"
        )

   
    expected_total = (
        invoice_data.subtotal
        + invoice_data.tax_amount
        - invoice_data.discount_amount
    )

    if invoice_data.total_amount != expected_total:
        raise ValueError(
            "Total amount does not match "
            "subtotal + tax - discount"
        )

   
    allowed_statuses = {
        "Draft",
        "Pending",
        "Paid",
        "Cancelled",
        "Overdue",
    }

    if invoice_data.invoice_status not in allowed_statuses:
        raise ValueError(
            "Invalid invoice status"
        )

    return crud_create_invoice(
        db,
        invoice_data
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
        raise ValueError(
            "Invoice not found"
        )

  
    if invoice_data.invoice_date is not None:

        if invoice_data.invoice_date > date.today():
            raise ValueError(
                "Invoice date cannot be in the future"
            )

    if invoice_data.due_date is not None:

        invoice_date = (
            invoice_data.invoice_date
            if invoice_data.invoice_date is not None
            else invoice.invoice_date
        )

        if invoice_data.due_date < invoice_date:
            raise ValueError(
                "Due date cannot be before invoice date"
            )

    # Validate amounts
    if (
        invoice_data.subtotal is not None
        and invoice_data.subtotal < 0
    ):
        raise ValueError(
            "Subtotal cannot be negative"
        )

    if (
        invoice_data.tax_amount is not None
        and invoice_data.tax_amount < 0
    ):
        raise ValueError(
            "Tax amount cannot be negative"
        )

    if (
        invoice_data.discount_amount is not None
        and invoice_data.discount_amount < 0
    ):
        raise ValueError(
            "Discount amount cannot be negative"
        )

    if (
        invoice_data.total_amount is not None
        and invoice_data.total_amount < 0
    ):
        raise ValueError(
            "Total amount cannot be negative"
        )

  
    if invoice_data.invoice_status is not None:

        allowed_statuses = {
            "Draft",
            "Pending",
            "Paid",
            "Cancelled",
            "Overdue",
        }

        if invoice_data.invoice_status not in allowed_statuses:
            raise ValueError(
                "Invalid invoice status"
            )

    return crud_update_invoice(
        db,
        invoice_id,
        invoice_data
    )


def delete_invoice(
    db: Session,
    invoice_id: int
):
    invoice = get_invoice(
        db,
        invoice_id
    )

    if not invoice:
        raise ValueError(
            "Invoice not found"
        )

    return crud_delete_invoice(
        db,
        invoice_id
    )