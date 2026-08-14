from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class InvoiceCreate(BaseModel):
    billing_id: int
    invoice_number: str
    invoice_date: date
    due_date: date | None = None
    total_amount: Decimal
    status: str = "unpaid"


class InvoiceUpdate(BaseModel):
    invoice_date: date | None = None
    due_date: date | None = None
    total_amount: Decimal | None = None
    status: str | None = None


class InvoiceResponse(BaseModel):
    id: int
    billing_id: int
    invoice_number: str
    invoice_date: date
    due_date: date | None
    total_amount: Decimal
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)