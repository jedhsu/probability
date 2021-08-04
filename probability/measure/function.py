from dataclasses import dataclass
from typing import Generic, Hashable, Mapping, TypeVar

import bidict
from sympy import Expr, Interval

from .measurable import MeasurableSpace, SigmaAlgebra

T = TypeVar("T", bound=Hashable)

__all__ = ["MeasurableFunction"]

"""

Measurable Function

"""

PositiveReals = Interval(0, None)


class MeasurableFunction(
    Mapping[SigmaAlgebra[T], PositiveReals],
    Generic[T],
):
    def __call__(self):
        pass
        # return self.getitem(

    # [Conditions]              for type membership

    def empty_set_into_zero(self):
        pass

    def countably_additive(self):
        pass
