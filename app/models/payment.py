from datetime import date, datetime

from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
)

from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class PaymentMethod(Base):
    __tablename__ = "payment_methods"

    method_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey(
            "customers.customer_id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    payment_type: Mapped[str] = mapped_column(
        SQLEnum(
            "UPI",
            "Credit Card",
            "Debit Card",
            "Net Banking",
            "Wallet"
        ),
        nullable=False
    )

    provider_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    account_number: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    expiry_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    is_default: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    status: Mapped[str] = mapped_column(
        SQLEnum("Active", "Inactive"),
        default="Active",
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    customer = relationship(
        "Customer",
        back_populates="payment_methods"
    )

    payments = relationship(
        "Payment",
        back_populates="payment_method"
    )


class Payment(Base):
    __tablename__ = "payments"

    payment_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey(
            "customers.customer_id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    method_id: Mapped[int] = mapped_column(
        ForeignKey(
            "payment_methods.method_id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    amount: Mapped[float] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        default="INR"
    )

    payment_status: Mapped[str] = mapped_column(
        SQLEnum(
            "Pending",
            "Success",
            "Failed",
            "Refunded"
        ),
        default="Pending",
        nullable=False
    )

    payment_reference: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
        nullable=True
    )

    payment_date: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    remarks: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    customer = relationship(
        "Customer",
        back_populates="payments"
    )

    payment_method = relationship(
        "PaymentMethod",
        back_populates="payments"
    )

    transactions = relationship(
        "Transaction",
        back_populates="payment",
        cascade="all, delete-orphan"
    )

    logs = relationship(
        "PaymentLog",
        back_populates="payment",
        cascade="all, delete-orphan"
    )


class PaymentLog(Base):
    __tablename__ = "payment_logs"

    log_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    payment_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "payments.payment_id",
            ondelete="CASCADE"
        ),
        nullable=True
    )

    transaction_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "transactions.transaction_id",
            ondelete="CASCADE"
        ),
        nullable=True
    )

    log_message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    log_level: Mapped[str] = mapped_column(
        SQLEnum(
            "INFO",
            "WARNING",
            "ERROR"
        ),
        default="INFO",
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    payment = relationship(
        "Payment",
        back_populates="logs"
    )

    transaction = relationship(
        "Transaction",
        back_populates="logs"
    )