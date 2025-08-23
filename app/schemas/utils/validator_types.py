from typing import Annotated
from pydantic import StringConstraints, AfterValidator, SecretStr
from .validators import password_strength_validator

# Name type with length constraints
Name = Annotated[str, StringConstraints(min_length=2, max_length=50)]

# Password type with strength validation
StrongPassword = Annotated[SecretStr, AfterValidator(password_strength_validator)]
