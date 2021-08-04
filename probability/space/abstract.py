"""

    *Abstract Space*

  An arbitrary mathematical space with countably infinite elements.

  (We first simplify by restricting to finite case.)

"""
from dataclasses import dataclass

from typing import Collection
from typing import Generic
from typing import Hashable
from typing import Iterator
from typing import Sequence
from typing import TypeVar

from sympy import Symbol
from sympy.sets.fancysets import Naturals0
from sympy.sets.sets import FiniteSet, Set


__all__ = ["AbstractSpace"]

# [TODO] this typing impl can be cleaner


T = TypeVar("T", bound=Hashable)


# @dataclass(frozen=True)
class AbstractSpace(
    FiniteSet,
    Generic[T],
):
    def __init__(self, *args, **kwargs):
        super(AbstractSpace, self).__new__(FiniteSet, *args, **kwargs)

    # [Collection Protocol]  is this implicit?

    #     def __contains__(self, elt: T) -> bool:
    #         return self.contains(elt)

    #     def __iter__(self) -> Iterator[T]:
    #         raise NotImplementedError

    #     def __len__(self) -> int:
    #         return super().__len__()

    # [Display]

    symbol = Symbol("Omega")

    def __repr__(self) -> str:
        raise NotImplementedError


class Test:
    @staticmethod
    def integers():
        return AbstractSpace(1, 2, 3)
