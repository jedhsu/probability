from ..aspace import AbstractSpace, Set, Test


class TestAbstractSpace:
    def test_init(self):
        aspace = Test.integers()

        assert isinstance(aspace, AbstractSpace)
        assert isinstance(aspace, Set)

        assert len(aspace) == 3
