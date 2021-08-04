"""

    *Measurable Space*

"""

from dataclasses import dataclass
from typing import Generic
from typing import Hashable
from typing import TypeVar

from sympy import Symbol

from .algebra import SigmaAlgebra

__all__ = ["MeasurableSpace"]

# [TODO] this typing impl can be cleaner
# [TODO] think you neeed a set base class that is typeful and inherits or encapsulates sympy.Set


T = TypeVar("T", bound=Hashable)


@dataclass
class BorelSet(Interval):
    pass


@dataclass
class MeasurableSpace(Generic[T]):
    omega: set[T]
    algebra: SigmaAlgebra
