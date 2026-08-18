from fastapi import HTTPException, status


class BillingException(Exception):
    """Base exception for billing application."""
    pass


class NotFoundException(BillingException):
    """Raised when requested resource is not found."""
    pass


class ValidationException(BillingException):
    """Raised when business validation fails."""
    pass


class DuplicateException(BillingException):
    """Raised when duplicate record is detected."""
    pass


class PaymentException(BillingException):
    """Raised when payment operation fails."""
    pass


class TransactionException(BillingException):
    """Raised when transaction operation fails."""
    pass


class InvoiceException(BillingException):
    """Raised when invoice operation fails."""
    pass


def not_found(message: str):
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=message
    )


def bad_request(message: str):
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=message
    )


def conflict(message: str):
    return HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=message
    )


def internal_server_error(
    message: str = "Internal server error"
):
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=message
    )