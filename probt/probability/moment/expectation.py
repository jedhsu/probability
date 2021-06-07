"""

Expectation, the first moment.

"""
test
from typing import Any, Sequence

from .base import Moment


class Expectation(Moment):
    @classmethod
    def __class_getitem__(cls, items: Sequence[Any]):
        assert 1 == 2, items
        return 1
