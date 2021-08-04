"""

    *Indicator Function*

  Dirac delta function.

"""
from typing import Generic, Hashable, Literal, Mapping, TypeVar

from sympy import Symbol

from .space import AbstractSpace

T = TypeVar("T", bound=Hashable)


class IndicatorFunction(
    Mapping[AbstractSpace, Literal[0, 1]],
    Generic[T],
):
    # [TODO] clarify the set[T] typing

    # [Display]

    symbol = Symbol("1")

    def __repr__(self):
        pass
