from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.crud.payment import (
    get_payment_method,
    get_payment_methods,
    get_payment,
    get_payments,
    get_payment_logs,
)

from app.schemas.payment import (
    PaymentMethodCreate,
    PaymentMethodUpdate,
    PaymentMethodResponse,
    PaymentCreate,
    PaymentUpdate,
    PaymentResponse,
    PaymentLogCreate,
    PaymentLogResponse,
)

from app.services.payment_service import (
    create_payment_method,
    update_payment_method,
    delete_payment_method,
    create_payment,
    update_payment,
    delete_payment,
    create_payment_log,
)


router = APIRouter(
    prefix="/billing/payments",
    tags=["Payments"]
)


@router.post(
    "/methods",
    response_model=PaymentMethodResponse,
    status_code=status.HTTP_201_CREATED
)
def create_payment_method_api(
    method_data: PaymentMethodCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_payment_method(
            db,
            method_data
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc)
        )


@router.get(
    "/methods",
    response_model=list[PaymentMethodResponse]
)
def get_payment_methods_api(
    customer_id: int | None = None,
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

    return get_payment_methods(
        db,
        customer_id=customer_id,
        skip=skip,
        limit=limit
    )


@router.get(
    "/methods/{method_id}",
    response_model=PaymentMethodResponse
)
def get_payment_method_api(
    method_id: int,
    db: Session = Depends(get_db)
):
    payment_method = get_payment_method(
        db,
        method_id
    )

    if not payment_method:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Payment method not found"
        )

    return payment_method


@router.put(
    "/methods/{method_id}",
    response_model=PaymentMethodResponse
)
def update_payment_method_api(
    method_id: int,
    method_data: PaymentMethodUpdate,
    db: Session = Depends(get_db)
):
    try:
        return update_payment_method(
            db,
            method_id,
            method_data
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc)
        )


@router.delete(
    "/methods/{method_id}",
    response_model=PaymentMethodResponse
)
def delete_payment_method_api(
    method_id: int,
    db: Session = Depends(get_db)
):
    try:
        return delete_payment_method(
            db,
            method_id
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc)
        )


@router.post(
    "",
    response_model=PaymentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_payment_api(
    payment_data: PaymentCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_payment(
            db,
            payment_data
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc)
        )


@router.get(
    "",
    response_model=list[PaymentResponse]
)
def get_payments_api(
    customer_id: int | None = None,
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

    return get_payments(
        db,
        customer_id=customer_id,
        skip=skip,
        limit=limit
    )


@router.post(
    "/logs",
    response_model=PaymentLogResponse,
    status_code=status.HTTP_201_CREATED
)
def create_payment_log_api(
    log_data: PaymentLogCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_payment_log(
            db,
            log_data
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc)
        )


@router.get(
    "/logs",
    response_model=list[PaymentLogResponse]
)
def get_payment_logs_api(
    payment_id: int | None = None,
    transaction_id: int | None = None,
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

    return get_payment_logs(
        db,
        payment_id=payment_id,
        transaction_id=transaction_id,
        skip=skip,
        limit=limit
    )


@router.get(
    "/{payment_id}",
    response_model=PaymentResponse
)
def get_payment_api(
    payment_id: int,
    db: Session = Depends(get_db)
):
    payment = get_payment(
        db,
        payment_id
    )

    if not payment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Payment not found"
        )

    return payment


@router.put(
    "/{payment_id}",
    response_model=PaymentResponse
)
def update_payment_api(
    payment_id: int,
    payment_data: PaymentUpdate,
    db: Session = Depends(get_db)
):
    try:
        return update_payment(
            db,
            payment_id,
            payment_data
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc)
        )


@router.delete(
    "/{payment_id}",
    response_model=PaymentResponse
)
def delete_payment_api(
    payment_id: int,
    db: Session = Depends(get_db)
):
    try:
        return delete_payment(
            db,
            payment_id
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc)
        )