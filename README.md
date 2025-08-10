# Goal-Driven Budgeting App API
An async personal budgeting app API built with [Quart](https://pgjones.gitlab.io/quart/), [SQLAlchemy](https://docs.sqlalchemy.org/en/20/), and [MySQL](https://www.mysql.com/).

## Features

- User registration and login with secure password hashing (Argon2)
- JWT-based authentication
- Async database access via SQLAlchemy and aiomysql
- Environment-based configuration
- Additional features are in development

## Project Structure

```
budgeting-app/
├── app/
│   ├── auth/           # Authentication utilities (JWT, password hashing)
│   ├── models/         # SQLAlchemy ORM models
│   ├── repositories/   # Database access logic
│   ├── routes/         # API endpoint definitions
│   ├── schemas/        # Pydantic schemas for requests/responses
│   ├── config.py       # App configuration
│   ├── db.py           # Database connection setup
│   └── main.py         # Quart app entrypoint
├── init_db.py          # Database initialization script
├── pyproject.toml      # Poetry configuration
├── .env.development    # Environment variables
└── README.md           # Project documentation
```