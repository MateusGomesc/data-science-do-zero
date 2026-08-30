from math import sqrt, pi, exp, erf
from matplotlib import pyplot as plt

def normal_pdf(x, mu=0, sigma=1.0):
    sqrt_two_pi = sqrt(2*pi)
    return exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma)

def normal_cdf(x, mu=0, sigma=1.0):
    return (1 + erf((x-mu) / sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    # Caso não seja o padrão, computa o padrão e redimensiona
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0
    hi_z, hi_p = 10.0, 0

    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p: # Valor no eixo y abaixo do esperado, aumenta inferiores
            low_z, low_p = mid_z, mid_p
        elif mid_p > p: # Valor no eixo y acima do esperado, abaixa superiores
            hi_z, hi_p = mid_z, mid_p
        else:
            break # Achou o resultado preciso

    return mid_z

# Testes gráficos das funções

# xs = [x / 10.0 for x in range(-50, 50)]
# plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
# plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
# plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
# plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
# plt.legend()
# plt.title("Diversas Funções de Densidade de Probabilidades Normais")
# plt.show()

# xs = [x / 10.0 for x in range(-50, 50)]
# plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
# plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
# plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
# plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
# plt.legend(loc=4)
# plt.title("Diversas Funções de Densidade de Distribuição Cumulativa")
# plt.show()