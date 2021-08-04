from typing import Generic, TypeVar

from ..measure import MeasureSpace
from .distribution import Distribution

"""

Random Variable

When measurable functions restricted to a codomain of [0, 1], they are
considered as random variables operating on a probability space.

"""

__all__ = ["RandomVariable"]

T = TypeVar("T")


class RandomVariable(Generic[T], Distribution):
    pass


class ProbabilitySpace(MeasureSpace):
    pass
