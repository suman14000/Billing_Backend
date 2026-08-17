from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.payment import (
    PaymentCreate,
    PaymentStatusUpdate,
    PaymentResponse,
)
from app.services import payment_service
from app.crud import payment as payment_crud


router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


@router.post(
    "/",
    response_model=PaymentResponse,
    status_code=201
)
def create_payment(
    payment_data: PaymentCreate,
    db: Session = Depends(get_db)
):
    return payment_service.create_payment(
        db,
        payment_data
    )


@router.put(
    "/{payment_id}/status",
    response_model=PaymentResponse
)
def update_payment_status(
    payment_id: int,
    payment_data: PaymentStatusUpdate,
    db: Session = Depends(get_db)
):
    payment = payment_service.update_payment_status(
        db,
        payment_id,
        payment_data
    )

    if not payment:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    return payment


@router.get(
    "/{payment_id}",
    response_model=PaymentResponse
)
def get_payment(
    payment_id: int,
    db: Session = Depends(get_db)
):
    payment = payment_crud.get_payment_by_id(
        db,
        payment_id
    )

    if not payment:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    return payment


@router.get(
    "/transaction/{transaction_id}",
    response_model=PaymentResponse
)
def get_payment_by_transaction(
    transaction_id: str,
    db: Session = Depends(get_db)
):
    payment = payment_crud.get_payment_by_transaction_id(
        db,
        transaction_id
    )

    if not payment:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return payment


@router.get(
    "/history/{billing_id}",
    response_model=list[PaymentResponse]
)
def get_payment_history(
    billing_id: int,
    db: Session = Depends(get_db)
):
    return payment_service.get_payment_history(
        db,
        billing_id
    )
