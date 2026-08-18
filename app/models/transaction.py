from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
)

from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    payment_id: Mapped[int] = mapped_column(
        ForeignKey(
            "payments.payment_id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    transaction_type: Mapped[str] = mapped_column(
        SQLEnum(
            "Payment",
            "Refund"
        ),
        default="Payment",
        nullable=False
    )

    transaction_reference: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
        nullable=True
    )

    transaction_status: Mapped[str] = mapped_column(
        SQLEnum(
            "Initiated",
            "Completed",
            "Failed"
        ),
        default="Initiated",
        nullable=False
    )

    amount: Mapped[float | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    transaction_date: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    payment = relationship(
        "Payment",
        back_populates="transactions"
    )

    logs = relationship(
        "PaymentLog",
        back_populates="transaction"
    )