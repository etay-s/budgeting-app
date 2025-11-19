from typing import TypeVar, Mapping

T = TypeVar("T")

Response = tuple[T, int] | tuple[T, int, Mapping[str, str]]
