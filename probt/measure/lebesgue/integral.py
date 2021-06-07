"""

Lebesgue Integral.

"""

# from sympy import Integral, Symbol
# from sympy.integrals.transforms import IntegralTransform

from ..function import MeasurableFunction
from ..measurable import Measurable
from .measure import Measure


class Integrate:
    # def integrate(
    def integrate_simple_function_over_measurable_set(fn: Measurable, E: MeasurableSet):
        pass

    def integrate_measurable_nonnegative_function(self):
        pass

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
