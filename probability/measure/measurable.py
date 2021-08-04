__all__ = [
    "AbstractSpace",
    "SigmaAlgebra",
    "MeasureSpace",
]

from dataclasses import dataclass

from typing import Generic
from typing import Hashable
from typing import TypeVar

from sympy import Symbol

T = TypeVar("T", bound=Hashable)

# [TODO] this typing impl can be cleaner


@dataclass
class BorelSet(Interval):
    pass


# MeasurableSet


@dataclass
class MeasurableSpace(Generic[T]):
    # [TODO] thinking about capitalizing these given context, though goes against convention
    omega: set[T]
    sigma_algebra: SigmaAlgebra[T]
