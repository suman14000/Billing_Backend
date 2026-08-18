from sqlalchemy.orm import Session

from app.crud.billing import (
    create_user as crud_create_user,
    get_user_by_email,
    create_customer as crud_create_customer,
    get_customer_by_email,
    update_customer as crud_update_customer,
    delete_customer as crud_delete_customer,
)

from app.schemas.billing import (
    UserCreate,
    CustomerCreate,
    CustomerUpdate,
)


def create_user(
    db: Session,
    user_data: UserCreate
):
    
    existing_user = get_user_by_email(
        db,
        user_data.email
    )

    if existing_user:
        raise ValueError(
            "User with this email already exists"
        )

    return crud_create_user(
        db,
        user_data
    )


def create_customer(
    db: Session,
    customer_data: CustomerCreate
):
   
    existing_customer = get_customer_by_email(
        db,
        customer_data.email
    )

    if existing_customer:
        raise ValueError(
            "Customer with this email already exists"
        )

    return crud_create_customer(
        db,
        customer_data
    )


def update_customer(
    db: Session,
    customer_id: int,
    customer_data: CustomerUpdate
):
   

    if customer_data.email:
        existing_customer = get_customer_by_email(
            db,
            customer_data.email
        )

        if (
            existing_customer
            and existing_customer.customer_id != customer_id
        ):
            raise ValueError(
                "Customer with this email already exists"
            )

    customer = crud_update_customer(
        db,
        customer_id,
        customer_data
    )

    if not customer:
        raise ValueError(
            "Customer not found"
        )

    return customer


def delete_customer(
    db: Session,
    customer_id: int
):
    customer = crud_delete_customer(
        db,
        customer_id
    )

    if not customer:
        raise ValueError(
            "Customer not found"
        )

    return customer