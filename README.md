# Goal-Driven Budgeting App API

An async personal budgeting app API built with [Quart](https://pgjones.gitlab.io/quart/), [SQLAlchemy](https://docs.sqlalchemy.org/en/20/), and [MySQL](https://www.mysql.com/), demonstrating modern Python development practices and robust CI/CD implementation.

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
├── scripts/
│   └── pre-push      # Git hooks for local development
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
3. Set up pre-push hooks:
   ```bash
   cp scripts/pre-push .git/hooks/
   chmod +x .git/hooks/pre-push
   ```
4. Configure environment variables
5. Initialize the database:
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

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[MIT License](LICENSE)