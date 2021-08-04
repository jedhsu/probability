"""

Expectation, the first moment.

"""

from typing import Any, Optional, Sequence

from sympy import Symbol

from ..randvar import RandomVariable
from .base import Moment


class _Symbolic_:
    base = Symbol("E")

    def symbol(
        self,
        randvar: RandomVariable,
        argument: Optional[Argument] = None,
        conditional: Optional[Conditional] = None,
    ) -> Symbol:
        return Symbol(f"{self.base}_{",".join([arg for arg in argment])})


class Expectation(Moment):
    @classmethod
    def __class_getitem__(cls, items: Sequence[Any]):
        assert 1 == 2, items
        return 1
