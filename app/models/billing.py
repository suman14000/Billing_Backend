from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database import base


class billing(base):

    __tablename__ = "billing"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    customer_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    customer_email: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    customer_phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    billing_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    subtotal: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=0
    )

    tax: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=0
    )

    discount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=0
    )

    total_amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
        default=0
    )

    billing_status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="pending"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    invoices = relationship(
        "invoice",
        back_populates="billing",
        cascade="all, delete-orphan"
    )
