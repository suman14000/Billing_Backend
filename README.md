# 💳 Billing Backend

## 📌 Project Overview

The **Billing Backend** is a FastAPI-based backend system developed to manage billing operations such as Payments, Transactions, Invoices, Validation, API Integration, and Testing.

The project uses **MySQL** as the database and **Swagger UI** for API testing and verification.

---

## 🚀 Billing Backend Modules

- 💳 Payment Management
- 🔄 Transaction Management
- 🧾 Invoice Creation & Management
- 🗄️ Billing Database & Models
- 🔌 Billing API Integration
- 🛡️ Validation & Error Handling
- 🧪 API Testing & Bug Fixing
- 🔀 Code Review, GitHub PR & Merge

---

## 👥 Team Members & Responsibilities

| Team Member | Responsibility |
|---|---|
| **Sumanth M T** | Billing Database & Models |
| **Surisetty Kamesh** | Billing CRUD APIs |
| **V Deepa** | Invoice Creation & Management |
| **Addhuru Poojitha** | Payment Status & Transaction Logic |
| **Ilavarasan Palanisamy** | Billing API Integration |
| **K Parisayram** | Billing Validation & Error Handling |
| **Kadirimangalam Nikhilsai** | API Testing & Bug Fixing |
| **Naganaboina Sum** | Code Review, GitHub PR & Merge |

---

## 🧩 Team Contributions

### 🗄️ Sumanth M T
Responsible for the **Billing Database & Models**, including database structure and backend model requirements.

### 🔧 Surisetty Kamesh
Responsible for developing **Billing CRUD APIs** for creating, retrieving, updating, and managing billing records.

### 🧾 V Deepa
Responsible for **Invoice Creation & Management**, including invoice-related API functionality.

### 💳 Addhuru Poojitha
Responsible for **Payment Status & Transaction Logic**, handling payment states and transaction-related operations.

### 🔌 Ilavarasan Palanisamy
Responsible for **Billing API Integration** and connecting billing APIs with the required backend components.

### 🛡️ K Parisayram
Responsible for **Billing Validation & Error Handling**, including request validation and handling invalid API inputs.

### 🧪 Kadirimangalam Nikhilsai
Responsible for **API Testing & Bug Fixing**.

Major activities include:

- Testing Billing APIs using Swagger UI
- Testing Payments APIs
- Testing Transaction APIs
- Testing Invoice APIs
- Verifying request and response data
- Checking database records using MySQL Workbench
- Identifying API errors
- Fixing bugs
- Re-testing corrected APIs
- Verifying successful database updates

### 🔀 Naganaboina Sum
Responsible for **Code Review, GitHub Pull Requests & Merge**, ensuring team code is reviewed and properly integrated.

---

## 🧪 API Testing

The Billing Backend APIs were tested using **Swagger UI**.

### Payments

```text
POST   /payments/billing/payments
GET    /payments/billing/payments
PUT    /payments/billing/payments/{payment_id}
POST   /payments/billing/payments/logs