from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()

def init_db():
    from app.models.billing import User, Customer
    from app.models.payment import PaymentMethod, Payment, PaymentLog
    from app.models.transaction import Transaction
    from app.models.invoice import Invoice

    Base.metadata.create_all(
        bind=engine
    )