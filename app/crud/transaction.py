from sqlalchemy.orm import Session

from app.models.transaction import Transaction

from app.schemas.transaction import (
    TransactionCreate,
    TransactionUpdate,
)

def create_transaction(
    db: Session,
    transaction_data: TransactionCreate
):
    transaction = Transaction(
        payment_id=transaction_data.payment_id,
        transaction_type=transaction_data.transaction_type,
        transaction_reference=(
            transaction_data.transaction_reference
        ),
        transaction_status=(
            transaction_data.transaction_status
        ),
        amount=transaction_data.amount,
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction


def get_transaction(
    db: Session,
    transaction_id: int
):
    return (
        db.query(Transaction)
        .filter(
            Transaction.transaction_id == transaction_id
        )
        .first()
    )


def get_transactions(
    db: Session,
    payment_id: int | None = None,
    skip: int = 0,
    limit: int = 100
):
    query = db.query(Transaction)

    if payment_id is not None:
        query = query.filter(
            Transaction.payment_id == payment_id
        )

    return (
        query
        .offset(skip)
        .limit(limit)
        .all()
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
        return None

    update_data = transaction_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(transaction, field, value)

    db.commit()
    db.refresh(transaction)

    return transaction


def delete_transaction(
    db: Session,
    transaction_id: int
):
    transaction = get_transaction(
        db,
        transaction_id
    )

    if not transaction:
        return None

    db.delete(transaction)
    db.commit()

    return transaction