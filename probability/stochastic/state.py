"""

State space is defined from a measurable space equipped with a Borel algebra.

Indexer is equivalent to state transition mapping.

"""

from ..probability import ProbabilitySpace, RandomVariable

# [TODO] you can generalize to also measurable processes... which will be relevant for program analysis


class StateSpace(MeasurableSpace):
    indexer: set[RandomVariable]
