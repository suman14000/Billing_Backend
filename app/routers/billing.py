from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.billing import (
    BillingCreate,
    BillingUpdate,
    BillingResponse
)

from app.services.billing_service import (
    create_billing,
    get_all_billings,
    get_billing_by_id,
    update_billing,
    delete_billing
)


router = APIRouter(
    prefix="/billing",
    tags=["Billing"]
)


@router.post("/", response_model=BillingResponse)
def create_bill(
    billing: BillingCreate,
    db: Session = Depends(get_db)
):
    return create_billing(db, billing)


@router.get("/", response_model=list[BillingResponse])
def get_bills(
    db: Session = Depends(get_db)
):
    return get_all_billings(db)


@router.get("/{billing_id}", response_model=BillingResponse)
def get_bill(
    billing_id: int,
    db: Session = Depends(get_db)
):
    return get_billing_by_id(db, billing_id)


@router.put("/{billing_id}", response_model=BillingResponse)
def update_bill(
    billing_id: int,
    billing: BillingUpdate,
    db: Session = Depends(get_db)
):
    return update_billing(
        db,
        billing_id,
        billing
    )


@router.delete("/{billing_id}")
def delete_bill(
    billing_id: int,
    db: Session = Depends(get_db)
):
    return delete_billing(
        db,
        billing_id
    )
