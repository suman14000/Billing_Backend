from datetime import date, datetime
from decimal import Decimal, ROUND_HALF_UP
from typing import Any


def round_amount(
    amount: Decimal | float | int
) -> Decimal:
    """
    Round monetary value to 2 decimal places.
    """

    decimal_amount = Decimal(str(amount))

    return decimal_amount.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )


def clean_string(
    value: str | None
) -> str | None:
    """
    Remove unnecessary spaces from a string.
    """

    if value is None:
        return None

    value = value.strip()

    return value if value else None


def normalize_email(
    email: str
) -> str:
    """
    Normalize email before storing/searching.
    """

    return email.strip().lower()


def normalize_phone(
    phone: str | None
) -> str | None:
    """
    Remove spaces and common phone separators.
    """

    if phone is None:
        return None

    phone = phone.strip()
    phone = phone.replace(" ", "")
    phone = phone.replace("-", "")
    phone = phone.replace("(", "")
    phone = phone.replace(")", "")

    return phone


def get_current_date() -> date:
    """
    Return today's date.
    """

    return date.today()


def get_current_datetime() -> datetime:
    """
    Return current date and time.
    """

    return datetime.now()


def calculate_pagination(
    page: int,
    page_size: int
) -> tuple[int, int]:
    """
    Convert page/page_size into SQL offset/limit.
    """

    if page < 1:
        page = 1

    if page_size < 1:
        page_size = 10

    if page_size > 100:
        page_size = 100

    offset = (page - 1) * page_size

    return offset, page_size


def remove_none_values(
    data: dict[str, Any]
) -> dict[str, Any]:
    """
    Remove None values from dictionary.
    """

    return {
        key: value
        for key, value in data.items()
        if value is not None
    }


def get_update_data(
    schema_object: Any
) -> dict[str, Any]:
    """
    Convert Pydantic update schema into
    dictionary containing only provided fields.
    """

    if hasattr(
        schema_object,
        "model_dump"
    ):
        return schema_object.model_dump(
            exclude_unset=True
        )

    return schema_object.dict(
        exclude_unset=True
    )


def validate_positive_integer(
    value: int,
    field_name: str = "ID"
) -> int:
    """
    Validate positive integer values such as
    customer_id, payment_id, invoice_id, etc.
    """

    if value <= 0:
        raise ValueError(
            f"{field_name} must be greater than zero"
        )

    return value