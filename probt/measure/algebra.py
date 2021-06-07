from dataclasses import dataclass
from typing import Collection, Generic, Hashable, Iterator, TypeVar

from sympy.sets.fancysets import Naturals0
from sympy.sets.sets import Set

from .space import AbstractSpace

__all__ = ["SigmaAlgebra"]

# [TODO] get the power set typing right

"""
A sigma-algebra is a *collection of subsets* of Omega which is
closed under complement and finite union.

"""

T = TypeVar("T", bound=Hashable)


@dataclass
class SigmaAlgebra(
    Set,
    Collection[Collection[T]],
    Generic[T],
):
    space: AbstractSpace[T]

    # [Conditions]                  for type membership

    @property
    def _closed_under_generating_set(self) -> AbstractSpace[T]:
        return self.space

    @property
    def _closed_under_complement(self, elt: set[T]) -> set[T]:
        return elt.difference(self.space)

    @property
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
    def from_omega(omega: AbstractSpace[T]):
        pass


class _Examples:
    @staticmethod
    def binary():
        algebra = {(), AbstractSpace()}
        return algebra

    def power_set(self):
        algebra = AbstractSpace().powerset()

    def quad(self):
        pass
