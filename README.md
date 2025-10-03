# Goal-Driven Budgeting App API

An async personal budgeting app API demonstrating modern software engineering and development best practices, implemented in Python using [Quart](https://pgjones.gitlab.io/quart/), [SQLAlchemy](https://docs.sqlalchemy.org/en/20/), and [MySQL](https://www.mysql.com/).

## Key Technical Highlights

### Development Best Practices
- **Type Safety**: Comprehensive type hints and type checking to catch errors early
- **Code Quality**:
  - Strict linting configuration
  - Pre-push hooks for automated quality checks
  - Consistent code formatting
- **Testing Infrastructure**:
  - Extensive unit test coverage
  - Test-driven development approach
  - Automated test execution in CI pipeline

### CI/CD Pipeline
- **GitHub Actions Workflows** for:
  - Automated testing on push and PR
  - Code quality checks (linting, type checking)
  - Security scanning
- **Pull Request-based Development**:
  - Automated PR checks
  - Code review process
  - Branch protection rules

### Local Development Setup
- Pre-push hooks for:
  - Unit test execution
  - Linting checks
  - Type checking
  - Code formatting

## Core Features

- User registration and login with secure password hashing (Argon2)
- JWT-based authentication
- Async database access via SQLAlchemy and aiomysql
- Environment-based configuration
- Additional features are in development

## Project Architecture

```
budgeting-app/
├── app/
│   ├── auth/           # Authentication utilities (JWT, password hashing)
│   ├── models/         # SQLAlchemy ORM models
│   ├── repositories/   # Database access logic
│   ├── routes/         # API endpoint definitions
│   ├── schemas/        # Pydantic schemas for requests/responses
│   ├── config.py       # App configuration
│   ├── db.py          # Database connection setup
│   └── main.py        # Quart app entrypoint
├── tests/             # Unit tests directory
├── .github/
│   └── workflows/     # GitHub Actions CI/CD configurations
├── init_db.py         # Database initialization script
├── pyproject.toml     # Poetry configuration
├── .env.development   # Environment variables
└── README.md         # Project documentation
```

## Getting Started

1. Clone the repository
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Configure environment variables
4. Initialize the database:
   ```bash
   python init_db.py
   ```

## Development Workflow

1. Create a new branch for your feature
2. Make changes and commit
3. Push changes (pre-push hooks will run automatically)
4. Create a Pull Request
5. Wait for CI checks to pass and code review

## Quality Assurance

### Running Tests
```bash
poetry run pytest
```

### Type Checking
```bash
poetry run mypy .
```

### Linting
```bash
poetry run flake8
```

## License

[MIT License](LICENSE)