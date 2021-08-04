"""

    *Measurable Function*

"""

from dataclasses import dataclass

from typing import Generic
from typing import Hashable
from typing import Mapping
from typing import TypeVar

import bidict
from sympy import Expr
from sympy import Interval

from .measurable import MeasurableSpace
from .algebra import SigmaAlgebra

T = TypeVar("T", bound=Hashable)

__all__ = ["MeasurableFunction"]


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
