from sqlalchemy.orm import Session

from app.crud.transaction import (
    create_transaction as crud_create_transaction,
    get_transaction,
    update_transaction as crud_update_transaction,
    delete_transaction as crud_delete_transaction,
)

from app.crud.payment import get_payment

from app.schemas.transaction import (
    TransactionCreate,
    TransactionUpdate,
)


def create_transaction(
    db: Session,
    transaction_data: TransactionCreate
):

    payment = get_payment(
        db,
        transaction_data.payment_id
    )

    if not payment:
        raise ValueError(
            "Payment not found"
        )

    if (
        transaction_data.amount is not None
        and transaction_data.amount <= 0
    ):
        raise ValueError(
            "Transaction amount must be greater than zero"
        )

  
    if transaction_data.amount is None:
        transaction_data.amount = payment.amount

  
    allowed_types = {
        "Payment",
        "Refund"
    }

    if transaction_data.transaction_type not in allowed_types:
        raise ValueError(
            "Invalid transaction type"
        )

  
    allowed_statuses = {
        "Initiated",
        "Completed",
        "Failed"
    }

    if transaction_data.transaction_status not in allowed_statuses:
        raise ValueError(
            "Invalid transaction status"
        )

   
    if transaction_data.transaction_type == "Refund":

        if payment.payment_status != "Success":
            raise ValueError(
                "Only successful payments can be refunded"
            )

    return crud_create_transaction(
        db,
        transaction_data
    )


def update_transaction(
    db: Session,
    transaction_id: int,
    transaction_data: TransactionUpdate
):
    transaction = get_transaction(
        db,
        transaction_id
    )

    if not transaction:
        raise ValueError(
            "Transaction not found"
        )

  
    if (
        transaction_data.amount is not None
        and transaction_data.amount <= 0
    ):
        raise ValueError(
            "Transaction amount must be greater than zero"
        )

  
    if transaction_data.transaction_type is not None:

        allowed_types = {
            "Payment",
            "Refund"
        }

        if (
            transaction_data.transaction_type
            not in allowed_types
        ):
            raise ValueError(
                "Invalid transaction type"
            )


    if transaction_data.transaction_status is not None:

        allowed_statuses = {
            "Initiated",
            "Completed",
            "Failed"
        }

        if (
            transaction_data.transaction_status
            not in allowed_statuses
        ):
            raise ValueError(
                "Invalid transaction status"
            )

    return crud_update_transaction(
        db,
        transaction_id,
        transaction_data
    )


def delete_transaction(
    db: Session,
    transaction_id: int
):
    transaction = get_transaction(
        db,
        transaction_id
    )

    if not transaction:
        raise ValueError(
            "Transaction not found"
        )

    return crud_delete_transaction(
        db,
        transaction_id
    )