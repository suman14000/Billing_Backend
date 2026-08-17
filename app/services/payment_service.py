from sqlalchemy.orm import Session

from app.crud import payment as payment_crud
from app.schemas.payment import (
    PaymentCreate,
    PaymentStatusUpdate,
)


def create_payment(
    db: Session,
    payment_data: PaymentCreate
):
    return payment_crud.create_payment(
        db,
        payment_data
    )


def update_payment_status(
    db: Session,
    payment_id: int,
    payment_data: PaymentStatusUpdate
):
    payment = payment_crud.get_payment_by_id(
        db,
        payment_id
    )

    if not payment:
        return None

    payment.status = payment_data.status.value

    db.commit()
    db.refresh(payment)

    return payment


def get_payment_history(
    db: Session,
    billing_id: int
):
    return payment_crud.get_payment_history(
        db,
        billing_id
    )
