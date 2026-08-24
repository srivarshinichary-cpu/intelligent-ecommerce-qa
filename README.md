# Intelligent E-Commerce QA Automation Platform

An end-to-end QA automation framework for testing an e-commerce web application using UI automation, API testing, database validation, and automated test reporting.

The project is designed using industry-standard testing practices such as the Page Object Model (POM), PyTest fixtures, reusable utilities, API validation, SQL/SQLite database testing, and HTML reporting.

---

## 🚀 Project Overview

This project automates critical e-commerce workflows including:

- User login validation
- Invalid login validation
- Product selection
- Add-to-cart functionality
- Complete checkout workflow
- Order confirmation validation
- REST API testing
- Database validation
- Positive and negative test scenarios
- Automated HTML test reporting

The framework is designed to demonstrate how different QA testing layers can be integrated into a single automation project.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Selenium WebDriver | Web UI automation |
| PyTest | Test execution and framework |
| Requests | REST API testing |
| SQLite | Database testing |
| SQL | Database validation |
| Page Object Model | Maintainable UI automation |
| PyTest HTML | Test reporting |
| Git | Version control |
| GitHub | Source code management |

---

## 🏗️ Project Structure

```text
intelligent-ecommerce-qa/
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── checkout_page.py
│   └── order_confirmation_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_api.py
│   └── test_database.py
│
├── utils/
│   ├── __init__.py
│   ├── database.py
│   └── test_data.py
│
├── data/
│
├── screenshots/
│
├── reports/
│   └── report.html
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
