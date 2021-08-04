"""

    *Sigma Algebra*

  A sigma-algebra is a collection of subsets of Omega which is
  closed under complement and finite union.

"""

from __future__ import annotations
from dataclasses import dataclass

from typing import Collection
from typing import Generic
from typing import Hashable
from typing import Iterator
from typing import TypeVar

from sympy.sets.fancysets import Naturals0
from sympy.sets.sets import Set

from ..aspace import AbstractSpace

__all__ = ["SigmaAlgebra"]

# [TODO] get the power set typing right


T = TypeVar("T", bound=Hashable)


@dataclass
class SigmaAlgebra(
    Set,
    Collection[Collection[T]],
    Generic[T],
):
    root: AbstractSpace[T]

    # [Conditions]                  for type membership

    def _contains_root(self) -> AbstractSpace[T]:
        return self.root

    # [TODO] ugh sympy not extended for typing

    def _closed_under_complement(self, elt: set[T]) -> set[T]:
        return elt.difference(self.root)

    def _closed_under_countable_union(self, elements: set[set[T]]) -> set[T]:
        return set.union(elements)

    # [Collection Protocol]

    def __contains__(self) -> bool:
        raise NotImplementedError

    def __iter__(self) -> Iterator[T]:
        raise NotImplementedError

    def __len__(self) -> Naturals0:
        raise NotImplementedError

    # [Conversions]

    @staticmethod
    def from_omega(omega: AbstractSpace[T]) -> SigmaAlgebra:
        raise NotImplementedError

    # [Display]

    symbol = "\u2131"

    def __repr__(self) -> str:
        return f"{self.symbol}({self.space.symbol})"


class _Examples:
    @staticmethod
    def binary():
        algebra = {(), AbstractSpace()}
        return algebra

    def power_set(self):
        algebra = AbstractSpace().powerset()

    def quad(self):
        pass
