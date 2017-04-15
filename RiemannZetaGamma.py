import math
import sys


def gamma_int(n):  # gamma function defined for integer values
    try:
        return math.factorial(n - 1)
    except ValueError as error:
        raise error.with_traceback(sys.exc_info()[2])


def rzeta_series(z, N):  # riemann-zeta convergant series definition
    try:
        if z.real <= 1:
                raise ValueError("real component was less than or equal to 1")
        else:
            sum = 0
            for i in range(1, N):
                sum += i**(-z)
            return sum
    except ValueError as error:
        raise error.with_traceback(sys.exc_info()[2])
