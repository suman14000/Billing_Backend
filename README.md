# Billing Backend

A backend application for managing billing, invoices, and payments using FastAPI and MySQL.

## Features

- Billing management
- Invoice management
- Payment management
- MySQL database
- SQLAlchemy ORM
- REST API
- Swagger API documentation

## Technologies

- Python
- FastAPI
- SQLAlchemy
- MySQL
- PyMySQL
- Pydantic
- Uvicorn
- Python-dotenv

## Project Structure

```text
billing_management/
│
├── app/
│   ├── models/
│   ├── schemas/
│   ├── crud/
│   ├── routers/
│   ├── services/
│   ├── utils/
│   ├── database.py
│   ├── config.py
│   ├── dependencies.py
│   └── main.py
│
├── tests/
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── run.py
