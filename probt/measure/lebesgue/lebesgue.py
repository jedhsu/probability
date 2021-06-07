"""

Implementation of the Lebesgue integral.

"""

# from sympy import Integral, Symbol
# from sympy.integrals.transforms import IntegralTransform

from .measure import Measure

# f = Symbol("f")
# mu = Symbol("mu")
# E = Symbol("E")


# class LebesgueIntegral(IntegralTransform):
#     def _compute_transform(
#         f: Measurable,
#         mu: Measure,
#         set: MeasurableSet,
#     ):
#         pass

#     def _as_integral(
#         self,
#         f: Measurable,
#         mu: Measure,
#         set: Symbol("E"),
#     ):
#         return Integral(f, (mu, E))
