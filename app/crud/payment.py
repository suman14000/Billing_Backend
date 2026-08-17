import uuid

from sqlalchemy.orm import Session

from app.models import Payment
from app.schemas.payment import PaymentCreate


def generate_transaction_id():
    return f"TXN-{uuid.uuid4().hex[:12].upper()}"


def create_payment(
    db: Session,
    payment_data: PaymentCreate
):
    payment = Payment(
        billing_id=payment_data.billing_id,
        transaction_id=generate_transaction_id(),
        amount=payment_data.amount,
        payment_method=payment_data.payment_method,
        status="pending"
    )

    db.add(payment)
    db.commit()
    db.refresh(payment)

    return payment


def get_payment_by_id(
    db: Session,
    payment_id: int
):
    return (
        db.query(Payment)
        .filter(Payment.id == payment_id)
        .first()
    )


def get_payment_by_transaction_id(
    db: Session,
    transaction_id: str
):
    return (
        db.query(Payment)
        .filter(
            Payment.transaction_id == transaction_id
        )
        .first()
    )


def update_payment_status(
    db: Session,
    payment_id: int,
    status: str
):
    payment = get_payment_by_id(
        db,
        payment_id
    )

    if not payment:
        return None

    payment.status = status

    db.commit()
    db.refresh(payment)

    return payment


def get_payment_history(
    db: Session,
    billing_id: int
):
    return (
        db.query(Payment)
        .filter(
            Payment.billing_id == billing_id
        )
        .order_by(
            Payment.created_at.desc()
        )
        .all()
    )
