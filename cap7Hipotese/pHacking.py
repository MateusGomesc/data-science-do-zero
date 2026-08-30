from __future__ import division
from math import sqrt
from pValues import two_sided_p_values
from random import random, seed


def run_experiment():
    return [random() < 0.5 for _ in range(1000)]

def reject_fairness(experiment):
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531

#seed(0)
#experiments = [run_experiment() for _ in range(1000)]
#num_rejections = len([experiment for experiment in experiments if reject_fairness(experiment)])
#print(num_rejections)

def estimated_parameters(N, n):
    p = n/N
    sigma = sqrt(p * (1 - p) / N)
    return p, sigma

def a_b_test_statistic(N_A, n_A, N_B, n_B):
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / sqrt(sigma_A ** 2 + sigma_B ** 2)

z = a_b_test_statistic(1000, 200, 1000, 180)
print(two_sided_p_values(z))