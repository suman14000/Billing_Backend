from datetime import date
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database import Base


class Invoice(Base):

    __tablename__ = "invoice"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    billing_id: Mapped[int] = mapped_column(
        ForeignKey(
            "billing.id",
            ondelete="CASCADE"
        ),
        nullable=False,
        index=True
    )

    invoice_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True
    )

    invoice_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    due_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    total_amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="unpaid"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    billing = relationship(
        "Billing",
        back_populates="invoices"
    )

    payments = relationship(
        "Payment",
        back_populates="invoice",
        cascade="all, delete-orphan"
    )