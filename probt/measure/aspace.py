from dataclasses import dataclass
from typing import Collection, Generic, Hashable, Iterator, TypeVar

from sympy import Symbol
from sympy.sets.fancysets import Naturals0
from sympy.sets.sets import Set


__all__ = ["AbstractSpace"]

# [TODO] this typing impl can be cleaner


"""
An arbitrary mathematical space with countably infinite elements.

We simplify by restricting to finite case.

"""

T = TypeVar("T", bound=Hashable)


@dataclass(frozen=True)
class AbstractSpace(
    Set,
    Collection[T],
    Generic[T],
):
    # [Collection Protocol]

    def __contains__(self) -> bool:
        raise NotImplementedError

    def __iter__(self) -> Iterator[T]:
        raise NotImplementedError

    def __len__(self) -> Naturals0:
        raise NotImplementedError

    # [Display]

    symbol = Symbol("Omega")

    def __repr__(self) -> str:
        raise NotImplementedError
