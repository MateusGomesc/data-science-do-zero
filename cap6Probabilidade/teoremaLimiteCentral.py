from collections import Counter
from random import random
from matplotlib import pyplot as plt
from math import sqrt

from cap6Probabilidade.distNormal import normal_cdf


def bernoulli_trial(p):
    return 1 if random() < p else 0

def binomial(n,p):
    return sum(bernoulli_trial(p) for _ in range(n))

def make_hist(p,n,num_points):
    data = [binomial(n,p) for _ in range(num_points)]
    histogram = Counter(data)
    plt.bar(histogram.keys(), [v / num_points for v in histogram.values()], 0.8, color='0.75')
    mu = p*n
    sigma = sqrt(n*p*(1-p))
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i+0.5,mu,sigma) - normal_cdf(i-0.5,mu,sigma) for i in xs]
    plt.plot(xs,ys)
    plt.title("Distribuição Binomial vs. Aproximação Normal")
    plt.show()

make_hist(0.75, 100, 10000)