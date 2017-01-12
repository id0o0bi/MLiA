import math

def is_sqr(x):
    s = int(math.sqrt(x))
    return s*s == x

print filter(is_sqr, range(1, 101))