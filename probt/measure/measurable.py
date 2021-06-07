from dataclasses import dataclass
from typing import Generic, Hashable, TypeVar

from sympy import Symbol

T = TypeVar("T", bound=Hashable)

# [TODO] this typing impl can be cleaner

__all__ = [
    "AbstractSpace",
    "SigmaAlgebra",
    "MeasureSpace",
]


@dataclass
class BorelSet(Interval):
    pass


@dataclass
class MeasurableSpace(Generic[T]):
    omega: set[T]
    sigma_algebra: SigmaAlgebra[T]
