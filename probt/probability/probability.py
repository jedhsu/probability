from typing import Callable, TypeVar

from sympy import Symbol

from .event import Occurable, SigmaAlgebra
from .measurable import Measurable

T = TypeVar("T")


class Probability(float):
    def __init__(self, value: float):
        assert 0.0 <= value <= 1
        super(Probability, self).__new__(float, value)


class ProbabilityMeasure(
    Callable[[SigmaAlgebra[T]], Probability],
):
    symbol = Symbol("P")


class _Integrate_(ProbabilityMeasure):
    """
    A probability measure must be integratable.

    fn      measurable function
    mset    measurable set
    """

    # [TODO} what does the measurability of T include?
    def integrate(self, fn: Measurable[T], mset: set[Occurable[T]]):
        pass


# -- Aliases
Probabilistic = ProbabilityMeasure


class _EventSpaces_:
    @staticmethod
    def dice_roll():
        return EventSpace(
            {
                Occurable(1),
                Occurable(2),
                Occurable(3),
                Occurable(4),
                Occurable(5),
                Occurable(6),
            }
        )
