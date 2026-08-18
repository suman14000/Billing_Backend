from decimal import Decimal
import re

def validate_amount(
    amount: Decimal,
    field_name: str = "Amount"
) -> Decimal:

    if amount is None:
        raise ValueError(
            f"{field_name} is required"
        )

    if amount <= 0:
        raise ValueError(
            f"{field_name} must be greater than zero"
        )

    return amount


def validate_non_negative_amount(
    amount: Decimal,
    field_name: str = "Amount"
) -> Decimal:

    if amount is None:
        raise ValueError(
            f"{field_name} is required"
        )

    if amount < 0:
        raise ValueError(
            f"{field_name} cannot be negative"
        )

    return amount


def validate_email(email: str) -> str:

    if not email:
        raise ValueError(
            "Email is required"
        )

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(pattern, email):
        raise ValueError(
            "Invalid email address"
        )

    return email


def validate_phone(phone: str | None):

    if phone is None:
        return phone

    phone = phone.strip()

    if not phone:
        return None

    if not phone.isdigit():
        raise ValueError(
            "Phone number must contain only digits"
        )

    if len(phone) < 10 or len(phone) > 15:
        raise ValueError(
            "Phone number must contain 10 to 15 digits"
        )

    return phone


def validate_pincode(pincode: str | None):

    if pincode is None:
        return pincode

    pincode = pincode.strip()

    if not pincode.isdigit():
        raise ValueError(
            "Pincode must contain only digits"
        )

    if len(pincode) < 4 or len(pincode) > 10:
        raise ValueError(
            "Invalid pincode"
        )

    return pincode


def validate_status(
    status_value: str,
    allowed_statuses: set[str]
) -> str:

    if status_value not in allowed_statuses:
        raise ValueError(
            f"Invalid status. "
            f"Allowed values: "
            f"{', '.join(sorted(allowed_statuses))}"
        )

    return status_value


def validate_payment_type(
    payment_type: str
) -> str:

    allowed_types = {
        "UPI",
        "Credit Card",
        "Debit Card",
        "Net Banking",
        "Wallet",
    }

    if payment_type not in allowed_types:
        raise ValueError(
            "Invalid payment type"
        )

    return payment_type


def validate_transaction_type(
    transaction_type: str
) -> str:

    allowed_types = {
        "Payment",
        "Refund",
    }

    if transaction_type not in allowed_types:
        raise ValueError(
            "Invalid transaction type"
        )

    return transaction_type


def validate_invoice_status(
    invoice_status: str
) -> str:

    allowed_statuses = {
        "Draft",
        "Pending",
        "Paid",
        "Cancelled",
        "Overdue",
    }

    if invoice_status not in allowed_statuses:
        raise ValueError(
            "Invalid invoice status"
        )

    return invoice_status