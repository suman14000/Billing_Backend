from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class InvoiceBase(BaseModel):
    customer_id: int

    invoice_number: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    invoice_date: date

    due_date: date | None = None

    subtotal: Decimal = Field(
        default=0,
        ge=0
    )

    tax_amount: Decimal = Field(
        default=0,
        ge=0
    )

    discount_amount: Decimal = Field(
        default=0,
        ge=0
    )

    total_amount: Decimal = Field(
        default=0,
        ge=0
    )

    invoice_status: str = "Draft"

    notes: str | None = None


class InvoiceCreate(InvoiceBase):
    pass


class InvoiceUpdate(BaseModel):
    invoice_date: date | None = None

    due_date: date | None = None

    subtotal: Decimal | None = Field(
        default=None,
        ge=0
    )

    tax_amount: Decimal | None = Field(
        default=None,
        ge=0
    )

    discount_amount: Decimal | None = Field(
        default=None,
        ge=0
    )

    total_amount: Decimal | None = Field(
        default=None,
        ge=0
    )

    invoice_status: str | None = None

    notes: str | None = None


class InvoiceResponse(InvoiceBase):
    invoice_id: int

    created_at: datetime

    updated_at: datetime | None = None

    model_config = ConfigDict(
        from_attributes=True
    )