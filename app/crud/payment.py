from sqlalchemy.orm import Session

from app.models.payment import (
    PaymentMethod,
    Payment,
    PaymentLog,
)

from app.schemas.payment import (
    PaymentMethodCreate,
    PaymentMethodUpdate,
    PaymentCreate,
    PaymentUpdate,
    PaymentLogCreate,
)

def create_payment_method(
    db: Session,
    method_data: PaymentMethodCreate
):
    payment_method = PaymentMethod(
        customer_id=method_data.customer_id,
        payment_type=method_data.payment_type,
        provider_name=method_data.provider_name,
        account_number=method_data.account_number,
        expiry_date=method_data.expiry_date,
        is_default=method_data.is_default,
        status=method_data.status,
    )

    db.add(payment_method)
    db.commit()
    db.refresh(payment_method)

    return payment_method


def get_payment_method(
    db: Session,
    method_id: int
):
    return (
        db.query(PaymentMethod)
        .filter(
            PaymentMethod.method_id == method_id
        )
        .first()
    )


def get_payment_methods(
    db: Session,
    customer_id: int | None = None,
    skip: int = 0,
    limit: int = 100
):
    query = db.query(PaymentMethod)

    if customer_id is not None:
        query = query.filter(
            PaymentMethod.customer_id == customer_id
        )

    return (
        query
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_payment_method(
    db: Session,
    method_id: int,
    method_data: PaymentMethodUpdate
):
    payment_method = get_payment_method(
        db,
        method_id
    )

    if not payment_method:
        return None

    update_data = method_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(payment_method, field, value)

    db.commit()
    db.refresh(payment_method)

    return payment_method


def delete_payment_method(
    db: Session,
    method_id: int
):
    payment_method = get_payment_method(
        db,
        method_id
    )

    if not payment_method:
        return None

    db.delete(payment_method)
    db.commit()

    return payment_method

def create_payment(
    db: Session,
    payment_data: PaymentCreate
):
    payment = Payment(
        customer_id=payment_data.customer_id,
        method_id=payment_data.method_id,
        amount=payment_data.amount,
        currency=payment_data.currency,
        payment_status=payment_data.payment_status,
        payment_reference=payment_data.payment_reference,
        remarks=payment_data.remarks,
    )

    db.add(payment)
    db.commit()
    db.refresh(payment)

    return payment


def get_payment(
    db: Session,
    payment_id: int
):
    return (
        db.query(Payment)
        .filter(
            Payment.payment_id == payment_id
        )
        .first()
    )


def get_payments(
    db: Session,
    customer_id: int | None = None,
    skip: int = 0,
    limit: int = 100
):
    query = db.query(Payment)

    if customer_id is not None:
        query = query.filter(
            Payment.customer_id == customer_id
        )

    return (
        query
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_payment(
    db: Session,
    payment_id: int,
    payment_data: PaymentUpdate
):
    payment = get_payment(
        db,
        payment_id
    )

    if not payment:
        return None

    update_data = payment_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(payment, field, value)

    db.commit()
    db.refresh(payment)

    return payment


def delete_payment(
    db: Session,
    payment_id: int
):
    payment = get_payment(
        db,
        payment_id
    )

    if not payment:
        return None

    db.delete(payment)
    db.commit()

    return payment


def create_payment_log(
    db: Session,
    log_data: PaymentLogCreate
):
    payment_log = PaymentLog(
        payment_id=log_data.payment_id,
        transaction_id=log_data.transaction_id,
        log_message=log_data.log_message,
        log_level=log_data.log_level,
    )

    db.add(payment_log)
    db.commit()
    db.refresh(payment_log)

    return payment_log


def get_payment_logs(
    db: Session,
    payment_id: int | None = None,
    transaction_id: int | None = None,
    skip: int = 0,
    limit: int = 100
):
    query = db.query(PaymentLog)

    if payment_id is not None:
        query = query.filter(
            PaymentLog.payment_id == payment_id
        )

    if transaction_id is not None:
        query = query.filter(
            PaymentLog.transaction_id == transaction_id
        )

    return (
        query
        .offset(skip)
        .limit(limit)
        .all()
    )