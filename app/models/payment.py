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

from app.database import base


class payment(base):

    __tablename__ = "payment"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    invoice_id: Mapped[int] = mapped_column(
        ForeignKey(
            "invoice.id",
            ondelete="CASCADE"
        ),
        nullable=False,
        index=True
    )

    payment_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    payment_method: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    transaction_id: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
        nullable=True,
        index=True
    )

    payment_status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="pending"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    invoice = relationship(
        "invoice",
        back_populates="payments"
    )
