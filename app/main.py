from fastapi import FastAPI

from app.database import Base
from app.database import engine

from app.models import billing
from app.models import invoice
from app.models import payment
from app.routers.invoice import router as invoice_router

app = FastAPI(
    title="billing management api",
    version="1.0.0"
)

app.include_router(invoice_router)


Base.metadata.create_all(
    bind=engine
)

@app.get("/")
def root():

    return {
        "message": "billing management api is running"
    }
