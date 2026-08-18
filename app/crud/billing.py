from sqlalchemy.orm import Session

from app.models.billing import User, Customer
from app.schemas.billing import (
    UserCreate,
    CustomerCreate,
    CustomerUpdate,
)


def create_user(
    db: Session,
    user_data: UserCreate
):
    user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        phone=user_data.phone,
        password=user_data.password,
        role=user_data.role,
        status=user_data.status,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user(
    db: Session,
    user_id: int
):
    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )


def get_user_by_email(
    db: Session,
    email: str
):
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def get_users(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return (
        db.query(User)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_customer(
    db: Session,
    customer_data: CustomerCreate
):
    customer = Customer(
        customer_name=customer_data.customer_name,
        email=customer_data.email,
        phone=customer_data.phone,
        address=customer_data.address,
        city=customer_data.city,
        state=customer_data.state,
        country=customer_data.country,
        pincode=customer_data.pincode,
    )

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer


def get_customer(
    db: Session,
    customer_id: int
):
    return (
        db.query(Customer)
        .filter(Customer.customer_id == customer_id)
        .first()
    )


def get_customer_by_email(
    db: Session,
    email: str
):
    return (
        db.query(Customer)
        .filter(Customer.email == email)
        .first()
    )


def get_customers(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return (
        db.query(Customer)
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_customer(
    db: Session,
    customer_id: int,
    customer_data: CustomerUpdate
):
    customer = get_customer(db, customer_id)

    if not customer:
        return None

    update_data = customer_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(customer, field, value)

    db.commit()
    db.refresh(customer)

    return customer


def delete_customer(
    db: Session,
    customer_id: int
):
    customer = get_customer(db, customer_id)

    if not customer:
        return None

    db.delete(customer)
    db.commit()

    return customer