from typing import Annotated
from pydantic import StringConstraints, AfterValidator, SecretStr
from .validators import password_strength_validator

# Password type with strength validation
StrongPassword = Annotated[SecretStr, AfterValidator(password_strength_validator)]