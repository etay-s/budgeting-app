# Goal-Driven Budgeting App API

An async **Python** backend project showcasing modern engineering best practices — including **type safety**, **automated CI/CD**, and **pre-push quality checks**.  
Built with **Quart, SQLAlchemy, and MySQL**, this API demonstrates professional-grade development workflows using **Ruff, Black, Mypy, and Pytest**.

✅ **Highlights**
- Automated linting, formatting, typing, and testing via **GitHub Actions**  
- Local **pre-push hooks** running the same checks for full CI parity  
- Clean, modular architecture with async design and JWT-based authentication  

---

## 🧰 Tech Stack

| Category | Tools | Purpose |
|-----------|--------|----------|
| **Framework** | Quart | Async web backend (Flask-like) |
| **Database** | SQLAlchemy + aiomysql | Async ORM with MySQL |
| **Validation** | Pydantic | Request/response schemas |
| **Auth** | Argon2 + JWT | Secure password hashing and token auth |
| **Dev Tools** | Poetry | Dependency & environment management |
| **Quality & Tests** | Ruff, Black, Mypy, Pytest | Linting, formatting, typing, and testing |

---

## ⚙️ Automated Workflows

- **GitHub Actions** ensure consistent quality for every PR and push:
  - Linting (`ruff`)
  - Code formatting (`black`)
  - Type checking (`mypy`)
  - Unit tests (`pytest`)
- **Pre-push hooks** mirror these same checks locally, keeping local and CI environments aligned.
- **Branch protection rules** require passing checks before merge.

---

## 🧩 Core Features

- User signup and login with **Argon2** password hashing  
- **JWT authentication** and access control  
- **Async SQLAlchemy ORM** integration with MySQL  
- **Environment-based configuration** via `pydantic-settings`  

---

## 🗂️ Project Structure

```text
budgeting-app/

├── app/
│   ├── auth/           # JWT & password hashing
│   ├── models/         # ORM models
│   ├── repositories/   # Database layer
│   ├── routes/         # API endpoints
│   ├── schemas/        # Pydantic validation models
│   │   └── utils/      # Utility types and validators
│   ├── services/       # Business logic
│   ├── config.py       # App configuration
│   ├── db.py           # Database connection setup
│   └── main.py         # Quart app entry point
├── tests/unit/              # Unit tests
├── .github/workflows/       # CI configs
├── .pre-commit-config.yaml  # Pre-push hook config
├── init_db.py               # Database initialization script
└── pyproject.toml           # Poetry setup
```
## 🛠️ In Progress
- Expanding test coverage with a TDD approach
- Adding integration tests
- Dockerized local setup (planned)

## 🎯 Purpose
This project serves as a portfolio demonstration of:
- Building async Python APIs with clean architecture
- Implementing automated quality gates via CI/CD
- Maintaining reproducible and type-safe development environments