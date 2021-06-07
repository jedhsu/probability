from typing import Generic, Hashable, Literal, Mapping, TypeVar

from .measurable import AbstractSpace

T = TypeVar("T", bound=Hashable)


class IndicatorFunction(
    Mapping[AbstractSpace, Literal[0, 1]],
    Generic[T],
):
    # [TODO] clarify the set[T] typing
    pass
