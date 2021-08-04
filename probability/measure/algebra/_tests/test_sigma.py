from ..sigma import AbstractSpace, Set, SigmaAlgebra, Test


class TestSigmaAlgebra:
    def test_init(self):
        alg = SigmaAlgebra(AbstractSpace(1, 2, 3))

        assert isinstance(alg, SigmaAlgebra)
        assert isinstance(alg, Set)

        assert alg.space == AbstractSpace(1, 2, 3)

    def test_contains_generating_set(self):
        alg = SigmaAlgebra(AbstractSpace(1, 2, 3))

        assert alg in 
