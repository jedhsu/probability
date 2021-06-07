from dataclasses import dataclass
from typing import Generic, Hashable, TypeVar

from sympy import Symbol

from .algebra import SigmaAlgebra

__all__ = ["MeasurableSpace"]

# [TODO] this typing impl can be cleaner

"""

Measurable Space.

"""

T = TypeVar("T", bound=Hashable)


@dataclass
class BorelSet(Interval):
    pass


@dataclass
class MeasurableSpace(Generic[T]):
    omega: set[T]
    algebra: SigmaAlgebra
