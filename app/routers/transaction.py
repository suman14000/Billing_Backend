from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.crud.transaction import (
    get_transaction,
    get_transactions,
)

from app.schemas.transaction import (
    TransactionCreate,
    TransactionUpdate,
    TransactionResponse,
)

from app.services.transaction_service import (
    create_transaction,
    update_transaction,
    delete_transaction,
)


router = APIRouter(
    prefix="/billing/transactions",
    tags=["Transactions"]
)


@router.post(
    "",
    response_model=TransactionResponse,
    status_code=status.HTTP_201_CREATED
)
def create_transaction_api(
    transaction_data: TransactionCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_transaction(
            db,
            transaction_data
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc)
        )

@router.get(
    "",
    response_model=list[TransactionResponse]
)
def get_transactions_api(
    payment_id: int | None = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    if skip < 0:
        raise HTTPException(
            status_code=400,
            detail="skip cannot be negative"
        )

    if limit < 1 or limit > 100:
        raise HTTPException(
            status_code=400,
            detail="limit must be between 1 and 100"
        )

    return get_transactions(
        db,
        payment_id=payment_id,
        skip=skip,
        limit=limit
    )


@router.get(
    "/{transaction_id}",
    response_model=TransactionResponse
)
def get_transaction_api(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    transaction = get_transaction(
        db,
        transaction_id
    )

    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )

    return transaction


@router.put(
    "/{transaction_id}",
    response_model=TransactionResponse
)
def update_transaction_api(
    transaction_id: int,
    transaction_data: TransactionUpdate,
    db: Session = Depends(get_db)
):
    try:
        return update_transaction(
            db,
            transaction_id,
            transaction_data
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc)
        )


@router.delete(
    "/{transaction_id}",
    response_model=TransactionResponse
)
def delete_transaction_api(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    try:
        return delete_transaction(
            db,
            transaction_id
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc)
        )