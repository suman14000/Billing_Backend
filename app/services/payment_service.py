from sqlalchemy.orm import Session

from app.crud.payment import (
    create_payment_method as crud_create_payment_method,
    get_payment_method,
    get_payment_methods,
    update_payment_method as crud_update_payment_method,
    delete_payment_method as crud_delete_payment_method,
    create_payment as crud_create_payment,
    get_payment as crud_get_payment,
    update_payment as crud_update_payment,
    delete_payment as crud_delete_payment,
    create_payment_log as crud_create_payment_log,
)

from app.crud.billing import (
    get_customer,
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
  
    customer = get_customer(
        db,
        method_data.customer_id
    )

    if not customer:
        raise ValueError(
            "Customer not found"
        )


    if method_data.is_default:
        existing_methods = get_payment_methods(
            db,
            customer_id=method_data.customer_id
        )

        for method in existing_methods:
            method.is_default = False

        db.commit()

    return crud_create_payment_method(
        db,
        method_data
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
        raise ValueError(
            "Payment method not found"
        )


    if method_data.is_default is True:

        existing_methods = get_payment_methods(
            db,
            customer_id=payment_method.customer_id
        )

        for method in existing_methods:
            if method.method_id != method_id:
                method.is_default = False

        db.commit()

    return crud_update_payment_method(
        db,
        method_id,
        method_data
    )


def delete_payment_method(
    db: Session,
    method_id: int
):
    payment_method = get_payment_method(
        db,
        method_id
    )

    if not payment_method:
        raise ValueError(
            "Payment method not found"
        )

    return crud_delete_payment_method(
        db,
        method_id
    )


def create_payment(
    db: Session,
    payment_data: PaymentCreate
):
    # Check customer
    customer = get_customer(
        db,
        payment_data.customer_id
    )

    if not customer:
        raise ValueError(
            "Customer not found"
        )


    payment_method = get_payment_method(
        db,
        payment_data.method_id
    )

    if not payment_method:
        raise ValueError(
            "Payment method not found"
        )

    # Payment method must belong to same customer
    if (
        payment_method.customer_id
        != payment_data.customer_id
    ):
        raise ValueError(
            "Payment method does not belong to this customer"
        )

  
    if payment_method.status != "Active":
        raise ValueError(
            "Payment method is inactive"
        )

    if payment_data.amount <= 0:
        raise ValueError(
            "Payment amount must be greater than zero"
        )

    return crud_create_payment(
        db,
        payment_data
    )


def update_payment(
    db: Session,
    payment_id: int,
    payment_data: PaymentUpdate
):
    payment = crud_get_payment(
        db,
        payment_id
    )

    if not payment:
        raise ValueError(
            "Payment not found"
        )

    # Amount validation
    if (
        payment_data.amount is not None
        and payment_data.amount <= 0
    ):
        raise ValueError(
            "Payment amount must be greater than zero"
        )

    return crud_update_payment(
        db,
        payment_id,
        payment_data
    )


def delete_payment(
    db: Session,
    payment_id: int
):
    payment = crud_get_payment(
        db,
        payment_id
    )

    if not payment:
        raise ValueError(
            "Payment not found"
        )

    return crud_delete_payment(
        db,
        payment_id
    )


def create_payment_log(
    db: Session,
    log_data: PaymentLogCreate
):
 
    if (
        log_data.payment_id is None
        and log_data.transaction_id is None
    ):
        raise ValueError(
            "Payment ID or Transaction ID is required"
        )

   
    allowed_levels = {
        "INFO",
        "WARNING",
        "ERROR"
    }

    if log_data.log_level not in allowed_levels:
        raise ValueError(
            "Invalid log level"
        )

    return crud_create_payment_log(
        db,
        log_data
    )