import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv()


db_host = os.getenv("db_host")
db_port = os.getenv("db_port")
db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_name = os.getenv("db_name")

database_url = (
    f"mysql+pymysql://{db_user}:"
    f"{db_password.replace('@', '%40')}@"
    f"{db_host}:{db_port}/{db_name}"
)

engine = create_engine(
    database_url,
    pool_pre_ping=True,
    echo=False
)

sessionlocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = sessionlocal()

    try:
        yield db

    finally:
        db.close()
