from pydantic import BaseModel, EmailStr
from datetime import datetime


class BillingCreate(BaseModel):
    customer_name: str
    customer_email: EmailStr
    product_name: str
    quantity: int
    price: float
    payment_status: str = "Pending"


class BillingUpdate(BaseModel):
    customer_name: str
    customer_email: EmailStr
    product_name: str
    quantity: int
    price: float
    payment_status: str


class BillingResponse(BaseModel):
    id: int
    customer_name: str
    customer_email: str
    product_name: str
    quantity: int
    price: float
    total_amount: float
    payment_status: str
    created_at: datetime

    class Config:
        from_attributes = True
