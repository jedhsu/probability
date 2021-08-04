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


# MeasurableSet


@dataclass
class MeasurableSpace(Generic[T]):
    # [TODO] thinking about capitalizing these given context, though goes against convention
    omega: set[T]
    sigma_algebra: SigmaAlgebra[T]
