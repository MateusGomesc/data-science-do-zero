def uniform_pdf(x):
    return 1 if 0 <= x < 1 else 0

def uniform_cdf(x):
    if x < 0: return 0
    elif x < 1: return x
    else: return 1