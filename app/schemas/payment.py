from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class PaymentStatus(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"


class PaymentCreate(BaseModel):
    billing_id: int
    amount: float = Field(gt=0)
    payment_method: str


class PaymentStatusUpdate(BaseModel):
    status: PaymentStatus


class PaymentResponse(BaseModel):
    id: int
    billing_id: int
    transaction_id: str
    amount: float
    payment_method: str
    status: PaymentStatus
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
