from typing import NamedTuple, Generic, TypeVar, Optional, Mapping

T = TypeVar("T")

class Response(NamedTuple, Generic[T]):
    body: T
    status: Optional[int] = None
    headers: Optional[Mapping[str, str]] = None