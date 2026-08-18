from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class TransactionBase(BaseModel):
    payment_id: int

    transaction_type: str = "Payment"

    transaction_reference: str | None = None

    transaction_status: str = "Initiated"

    amount: Decimal | None = Field(
        default=None,
        gt=0
    )


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(BaseModel):
    transaction_type: str | None = None

    transaction_reference: str | None = None

    transaction_status: str | None = None

    amount: Decimal | None = Field(
        default=None,
        gt=0
    )


class TransactionResponse(TransactionBase):
    transaction_id: int

    transaction_date: datetime

    model_config = ConfigDict(
        from_attributes=True
    )