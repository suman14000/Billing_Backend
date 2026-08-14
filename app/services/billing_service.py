from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.billing import Billing
from app.schemas.billing import BillingCreate, BillingUpdate


def create_billing(
    db: Session,
    billing: BillingCreate
):
    total_amount = billing.quantity * billing.price

    new_billing = Billing(
        customer_name=billing.customer_name,
        customer_email=billing.customer_email,
        product_name=billing.product_name,
        quantity=billing.quantity,
        price=billing.price,
        total_amount=total_amount,
        payment_status=billing.payment_status
    )

    db.add(new_billing)
    db.commit()
    db.refresh(new_billing)

    return new_billing


def get_all_billings(db: Session):

    return db.query(Billing).all()


def get_billing_by_id(
    db: Session,
    billing_id: int
):
    billing = db.query(Billing).filter(
        Billing.id == billing_id
    ).first()

    if not billing:
        raise HTTPException(
            status_code=404,
            detail="Billing record not found"
        )

    return billing


def update_billing(
    db: Session,
    billing_id: int,
    billing_data: BillingUpdate
):
    billing = db.query(Billing).filter(
        Billing.id == billing_id
    ).first()

    if not billing:
        raise HTTPException(
            status_code=404,
            detail="Billing record not found"
        )

    billing.customer_name = billing_data.customer_name
    billing.customer_email = billing_data.customer_email
    billing.product_name = billing_data.product_name
    billing.quantity = billing_data.quantity
    billing.price = billing_data.price
    billing.payment_status = billing_data.payment_status

    # Recalculate total
    billing.total_amount = (
        billing_data.quantity * billing_data.price
    )

    db.commit()
    db.refresh(billing)

    return billing


def delete_billing(
    db: Session,
    billing_id: int
):
    billing = db.query(Billing).filter(
        Billing.id == billing_id
    ).first()

    if not billing:
        raise HTTPException(
            status_code=404,
            detail="Billing record not found"
        )

    db.delete(billing)
    db.commit()

    return {
        "message": "Billing record deleted successfully",
        "billing_id": billing_id
    }
