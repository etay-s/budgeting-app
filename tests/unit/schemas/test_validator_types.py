import pytest
from app.schemas.utils.validator_types import Name, StrongPassword
from pydantic import BaseModel, ValidationError, SecretStr

class NameModel(BaseModel):
    name: Name

class PasswordModel(BaseModel):
    password: StrongPassword

class TestNameType:
    @pytest.mark.parametrize(
        "name",
        [
            "",
            "A",
            "A" * 51,
        ]
    )
    def test_name_error(self, name):
        with pytest.raises(ValidationError):
            NameModel(name=name)

    @pytest.mark.parametrize(
        "name",
        [
            "John",
            "John Doe",
            "A" * 50,
        ]
    )
    def test_name_valid(self, name):
        model = NameModel(name=name)
        assert model.name == name

class TestStrongPasswordType:
    @pytest.mark.parametrize(
        "password",
        [
            "Short1!",
            "NoSpecialChar1",
        ]
    )
    def test_invalid_password_returns_error(self, password):
        with pytest.raises(ValidationError):
            PasswordModel(password=password)

    def test_valid_password_passes(self, strong_password):
        model = PasswordModel(password=strong_password)
        assert model.password == SecretStr(strong_password)