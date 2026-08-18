from fastapi import FastAPI

from app.config import settings
from app.database import init_db

from app.routers.billing import router as billing_router
from app.routers.payment import router as payment_router
from app.routers.transaction import router as transaction_router
from app.routers.invoice import router as invoice_router


app = FastAPI(
    title="Billing API Testing",
    version="1.0.0",
    description="Billing Backend API",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


@app.on_event("startup")
def startup_event():
    try:
        init_db()
        print("Database initialized successfully")
    except Exception as e:
        print(f"Database initialization error: {e}")


app.include_router(
    billing_router,
    prefix="/billing",
    tags=["Billing"]
)

app.include_router(
    payment_router,
    prefix="/payments",
    tags=["Payments"]
)

app.include_router(
    transaction_router,
    prefix="/transactions",
    tags=["Transactions"]
)

app.include_router(
    invoice_router,
    prefix="/invoices",
    tags=["Invoices"]
)


@app.get("/")
def root():
    return {
        "message": "Billing Backend is running",
        "version": "1.0.0"
    }


@app.get(
    "/health",
    tags=["Health"]
)
def health_check():
    return {
        "status": "healthy",
        "service": "Billing Backend"
    }