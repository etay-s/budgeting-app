import pytest
from pydantic import SecretStr
from app.schemas.utils.validators import password_strength_validator


class TestPasswordStrengthValidator:
    @pytest.mark.parametrize(
        "password",
        [
            "",
            "Short1!",
            "NoSpecialChar1",
            "nouppercase1!",
            "NOLOWERCASE1!",
            "NoNumbers!",
        ],
    )
    def test_invalid_password_returns_error(self, password):
        with pytest.raises(ValueError):
            password_strength_validator(SecretStr(password))

    def test_valid_password_passes(self, strong_password):
        secret_pw = SecretStr(strong_password)
        assert password_strength_validator(secret_pw) == secret_pw
