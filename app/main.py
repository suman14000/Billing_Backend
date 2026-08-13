from fastapi import FastAPI

from app.database import base
from app.database import engine

from app.models import billing
from app.models import invoice
from app.models import payment


app = FastAPI(
    title="billing management api",
    version="1.0.0"
)


base.metadata.create_all(
    bind=engine
)

@app.get("/")
def root():

    return {
        "message": "billing management api is running"
    }
