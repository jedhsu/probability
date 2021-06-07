from dataclasses import dataclass
from typing import Generic, Hashable, TypeVar

from sympy import Expr

from .function import MeasurableFunction
from .mspace import MeasurableSpace


__all__ = ["MeasureSpace"]

"""

Measure Space.

"""

T = TypeVar("T", bound=Hashable)


@dataclass(frozen=True)
class MeasureSpace(
    MeasurableSpace[T],
    Generic[T],
):
    """
    Inherits omega space and sigma-algebra.

    """

    _μ_: MeasurableFunction[T]

    # [Properties]

    @property
    def monotonic(self, set_A: set[T], set_B: set[T]) -> Optional[Expression]:
        """
        Monotonicity        A ⊂ B  implies  μ(A) <= μ(B)

        """
        # [TODO] Expression can be subtyped to Inequality

        if set_A in set_B:
            return Expr(self._μ_(set_A) <= self._μ_(set_B))

    # [TODO] use sympy structs for the countably infinite stuff

    @property
    def subadditive(self, set: set[T], countable_union_of_sets) -> Optional[Expression]:
        pass

    @property
    def continuous_from_below(self, seq) -> Optional[Expression]:
        pass

    @property
    def continuous_from_above(self, seq) -> Optional[Expression]:
        pass
