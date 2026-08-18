from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.crud.billing import (
    get_user,
    get_users,
    get_customer,
    get_customers,
)

from app.schemas.billing import (
    UserCreate,
    UserResponse,
    CustomerCreate,
    CustomerUpdate,
    CustomerResponse,
)

from app.services.billing_service import (
    create_user,
    create_customer,
    update_customer,
    delete_customer,
)


router = APIRouter(
    prefix="/billing",
    tags=["Billing"]
)


@router.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user_api(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_user(
            db,
            user_data
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc)
        )


@router.get(
    "/users",
    response_model=list[UserResponse]
)
def get_users_api(
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

    return get_users(
        db,
        skip=skip,
        limit=limit
    )


@router.get(
    "/users/{user_id}",
    response_model=UserResponse
)
def get_user_api(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = get_user(
        db,
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user



@router.post(
    "/customers",
    response_model=CustomerResponse,
    status_code=status.HTTP_201_CREATED
)
def create_customer_api(
    customer_data: CustomerCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_customer(
            db,
            customer_data
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc)
        )


@router.get(
    "/customers",
    response_model=list[CustomerResponse]
)
def get_customers_api(
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

    return get_customers(
        db,
        skip=skip,
        limit=limit
    )


@router.get(
    "/customers/{customer_id}",
    response_model=CustomerResponse
)
def get_customer_api(
    customer_id: int,
    db: Session = Depends(get_db)
):
    customer = get_customer(
        db,
        customer_id
    )

    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )

    return customer


@router.put(
    "/customers/{customer_id}",
    response_model=CustomerResponse
)
def update_customer_api(
    customer_id: int,
    customer_data: CustomerUpdate,
    db: Session = Depends(get_db)
):
    try:
        return update_customer(
            db,
            customer_id,
            customer_data
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc)
        )


@router.delete(
    "/customers/{customer_id}",
    response_model=CustomerResponse
)
def delete_customer_api(
    customer_id: int,
    db: Session = Depends(get_db)
):
    try:
        return delete_customer(
            db,
            customer_id
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc)
        )