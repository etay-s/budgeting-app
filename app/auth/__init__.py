from dataclasses import dataclass

from .jwt_utils import *
from .password_utils import *

@dataclass
class AuthHeaders:
    authorization: str