from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.billing import (
    BillingCreate,
    BillingUpdate,
    BillingResponse
)

from app.crud.billing import (
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

    bill = get_billing_by_id(db, billing_id)

    if not bill:
        raise HTTPException(
            status_code=404,
            detail="Billing record not found"
        )

    return bill


@router.put("/{billing_id}", response_model=BillingResponse)
def update_bill(
    billing_id: int,
    billing: BillingUpdate,
    db: Session = Depends(get_db)
):

    bill = update_billing(
        db,
        billing_id,
        billing
    )

    if not bill:
        raise HTTPException(
            status_code=404,
            detail="Billing record not found"
        )

    return bill


@router.delete("/{billing_id}")
def delete_bill(
    billing_id: int,
    db: Session = Depends(get_db)
):

    bill = delete_billing(
        db,
        billing_id
    )

    if not bill:
        raise HTTPException(
            status_code=404,
            detail="Billing record not found"
        )

    return {
        "message": "Billing record deleted successfully",
        "billing_id": billing_id
    }
