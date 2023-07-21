import numpy
import typing

def gaussian_product_theorem( center1: typing.List[float], exponent1: float, center2: typing.List[float], exponent2: float ) ->  typing.Tuple[typing.List[float], typing.List[float]]:
    gaussian_center      =   ((exponent1*center1)+(exponent2*center2))/(exponent1+exponent2)
    gaussian_exponent    =   (exponent1*exponent2)/(exponent1+exponent2)
    gaussian_integral    =   exp(-1*gaussian_exponent*numpy.dot(center1-center2, center1-center2))
    return (gaussian_center, gaussian_integral)

