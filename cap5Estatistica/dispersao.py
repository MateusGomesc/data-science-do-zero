from tendeciasCentrais import mean, quantile
from cap4AlgebraLinear.vetores import sum_squares
from math import sqrt

def data_range(x):
    return max(x) - min(x)

def de_mean(x):
    """Calcula os desvios dos numeros em relacao a media"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """variancia de dois ou mais elementos da amostra"""
    n = len(x)
    deviations = de_mean(x)
    return sum_squares(deviations) / (n-1)

def standard_deviation(x):
    return sqrt(variance(x))

def interquantile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)