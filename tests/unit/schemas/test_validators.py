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
        ]
    )
    def test_password_error(self, password):
        with pytest.raises(ValueError):
            password_strength_validator(SecretStr(password))

    def test_password_valid(self):
        assert password_strength_validator(SecretStr("StrongPass1!")) == SecretStr("StrongPass1!")