"""

A probability distribution is a probability measure such that P(Omega) == 1.

"""

from __future__ import annotations
from fractions import Fraction
from typing import Mapping

from .event import Event
from .measurable import Measurable
from .moment import Moment
from .probability import Probabilistic

__all__ = ["Distribution"]


class MomentGeneratingFunction:
    def moment_generating_function(self):
        return Expectation(exp(t * X))


class Distribution(
    Moment, MomentGeneratingFunction, Mapping[Probabilistic, Measurable]
):
    pass


class Cumulative(Distribution):
    """
    Cumulative distribution function.

    """

    def __call__(self):
        pass


"""

[Testing]

"""


class Distributions_:
    @staticmethod
    def dice_roll():
        dist = {
            Event(1): Fraction(1, 6),
            Event(2): Fraction(2, 6),
            Event(3): Fraction(3, 6),
            Event(4): Fraction(4, 6),
            Event(5): Fraction(5, 6),
            Event(6): Fraction(6, 6),
        }
        # [TODO] need to deal with the typing here
        return Distribution(dist)
