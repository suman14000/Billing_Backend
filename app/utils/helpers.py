from datetime import datetime
from uuid import uuid4


def generate_invoice_number() -> str:
    """
    Generate a readable unique invoice number.

    Example:
    INV-20260817-153045-A1B2
    """
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    random_part = uuid4().hex[:4].upper()

    return f"INV-{timestamp}-{random_part}"


def generate_transaction_id() -> str:
    """
    Generate a unique transaction ID.
    """
    return f"TXN-{uuid4().hex.upper()}"
