from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class PaymentMethodBase(BaseModel):
    customer_id: int
    payment_type: str
    provider_name: str | None = None
    account_number: str | None = None
    expiry_date: date | None = None
    is_default: bool = False
    status: str = "Active"


class PaymentMethodCreate(PaymentMethodBase):
    pass


class PaymentMethodUpdate(BaseModel):
    payment_type: str | None = None
    provider_name: str | None = None
    account_number: str | None = None
    expiry_date: date | None = None
    is_default: bool | None = None
    status: str | None = None


class PaymentMethodResponse(PaymentMethodBase):
    method_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class PaymentBase(BaseModel):
    customer_id: int
    method_id: int
    amount: Decimal = Field(..., gt=0)
    currency: str = Field(default="INR", max_length=10)
    payment_status: str = "Pending"
    payment_reference: str | None = None
    remarks: str | None = None


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    amount: Decimal | None = Field(default=None, gt=0)
    currency: str | None = Field(default=None, max_length=10)
    payment_status: str | None = None
    payment_reference: str | None = None
    remarks: str | None = None


class PaymentResponse(PaymentBase):
    payment_id: int
    payment_date: datetime

    model_config = ConfigDict(from_attributes=True)


class PaymentLogCreate(BaseModel):
    payment_id: int | None = None
    transaction_id: int | None = None
    log_message: str | None = None
    log_level: str = "INFO"


class PaymentLogResponse(PaymentLogCreate):
    log_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)