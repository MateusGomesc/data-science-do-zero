from __future__ import division

from math import sqrt

from cap6Probabilidade.distNormal import normal_cdf, inverse_normal_cdf


# Retorna média e desvio padrão
def normal_approximation_to_binomial(n,p):
    mu = p*n
    sigma = sqrt(p*(1-p)*n)
    return mu,sigma

# Probabilidade da variável estar abaixo de um limite
normal_probability_below = normal_cdf

# Probabilidade está acima do limite se não estiver acima
def normal_probability_above(lo, mu=0, sigma=1.0):
    return 1 - normal_cdf(lo, mu, sigma)

# Probabilidade da variável estar num intervalo
def normal_probability_between(lo, hi, mu=0, sigma=1.0):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# Probabilidade de estar fora do intervalo
def normal_probability_outside(lo, hi, mu=0, sigma=1.0):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

# Funções para encontrar os limites a partir de uma probabilidade
def normal_upper_bound(probability, mu=0, sigma=1.0):
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu=0, sigma=1.0):
    return inverse_normal_cdf(1-probability, mu, sigma)

def normal_two_side_bounds(probability, mu=0, sigma=1.0):
    tail_probability = (1-probability) / 2
    upper_bound = normal_lower_bound(tail_probability,mu,sigma)
    lower_bound = normal_upper_bound(tail_probability,mu,sigma)
    return lower_bound, upper_bound

# encontrando limites para p = 0,5
mu_0, sigma_0 = normal_approximation_to_binomial(1000,0.5)
lo, hi = normal_two_side_bounds(0.95, mu_0, sigma_0)

# Media e desvio padrão com p = 0,55
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

# Verificando probabilidade dessa media e desvio padrão estarem dentro dos limites (área de aceitação)
# Verifica na nova curva encontrada
type2_probability = normal_probability_between(lo,hi,mu_1,sigma_1)

# Verificando probabilidade dessa media e desvio padrão estarem fora dos limites
# Power nos diz o poder do teste em verificar se não vamos dizer que H₀ é verdadeiro, mas, na verdade, é falsa (Erro do tipo 2)
power = 1 - type2_probability


