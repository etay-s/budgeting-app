from pydantic import SecretStr

def password_strength_validator(secret: SecretStr) -> SecretStr:
    """Validate the strength of the password."""
    errors = []

    password = secret.get_secret_value()

    if len(password) < 8:
        errors.append("at least 8 characters long.")
    if not any(char.isdigit() for char in password):
        errors.append("at least one digit.")
    if not any(char.isupper() for char in password):
        errors.append("at least one uppercase letter.")
    if not any(char.islower() for char in password):
        errors.append("at least one lowercase letter.")
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password):
        errors.append("at least one special character.")

    if errors:
        raise ValueError("Password must contain: " + " ".join(errors))

    return password