"""

Lebesgue Integral.

"""

# from sympy import Integral, Symbol
# from sympy.integrals.transforms import IntegralTransform

from sympy import Symbol
from sympy.concrete.summations import Sum
from sympy.integrals import Integral

from ..function import MeasurableFunction
from ..measurable import Measurable
from ..space import MeasureSpace
from .measure import Measure

# [TODO] figure out the latex rendering

class Integrate(MeasureSpace):
    @classmethod
    def integrate_simple_function_over_measurable_set(cls, fn: Measurable, E: MeasurableSet) -> Sum:
        """
        Case where _φ_(omega) is simple, i.e. _φ_(omega) = \sum_{i=1} ^n a_i 1 A_i
        
        """

        return Sum(i, (1, n), Symbol("a_i") * cls._μ_(fn.A[i].intersect(E)))

    def integrate_measurable_nonnegative_function(self):
        

    def integrate_measruable_function(self):
        pass

    # [TODO] what is case 4? confused


class LebesgueIntegral(Integrate, IntegralTransform):
    def _compute_transform(
        _f_: Measurable,
        _μ_: MeasurableFunction,
        _E_: MeasurableSet,
    ):
        pass

    def _as_integral(
        self,
        f: Measurable,
        μ: Measure,
        set: Symbol("E"),
    ):
        return Integral(f, (mu, E))
