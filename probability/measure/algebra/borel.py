# just do power set for now. ez

__all__ = ["BorelAlgebra"]

from .sigma import SigmaAlgebra

# this step is not super explicitly necessary as long as you handle the borel mechanism implicitly


class BorelAlgebra(SigmalAlgebra):
    symbol = "B"


class BorelSpace:
    pass
