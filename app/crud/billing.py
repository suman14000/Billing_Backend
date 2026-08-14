from sqlalchemy.orm import Session
from app.models.billing import Billing
from app.schemas.billing import BillingCreate, BillingUpdate


def create_billing(db: Session, billing: BillingCreate):

    total = billing.quantity * billing.price

    new_bill = Billing(
        customer_name=billing.customer_name,
        customer_email=billing.customer_email,
        product_name=billing.product_name,
        quantity=billing.quantity,
        price=billing.price,
        total_amount=total,
        payment_status=billing.payment_status
    )

    db.add(new_bill)
    db.commit()
    db.refresh(new_bill)

    return new_bill


def get_all_billings(db: Session):

    return db.query(Billing).all()


def get_billing_by_id(db: Session, billing_id: int):

    return db.query(Billing).filter(
        Billing.id == billing_id
    ).first()


def update_billing(
    db: Session,
    billing_id: int,
    billing: BillingUpdate
):

    existing_bill = db.query(Billing).filter(
        Billing.id == billing_id
    ).first()

    if not existing_bill:
        return None

    existing_bill.customer_name = billing.customer_name
    existing_bill.customer_email = billing.customer_email
    existing_bill.product_name = billing.product_name
    existing_bill.quantity = billing.quantity
    existing_bill.price = billing.price

    existing_bill.total_amount = (
        billing.quantity * billing.price
    )

    existing_bill.payment_status = billing.payment_status

    db.commit()
    db.refresh(existing_bill)

    return existing_bill


def delete_billing(db: Session, billing_id: int):

    existing_bill = db.query(Billing).filter(
        Billing.id == billing_id
    ).first()

    if not existing_bill:
        return None

    db.delete(existing_bill)
    db.commit()

    return existing_bill
