"""

Random Variable

When measurable functions restricted to a codomain of [0, 1], they are
random variables operating on a probability space.

"""

from typing import Generic, TypeVar

from .distribution import Distribution


T = TypeVar("T")


class RandomVariable(Generic[T], Distribution):
    pass


class ProbabilitySpace(MeasureSpace):
    pass


# -- Alias
Stochastic = RandomVariable
