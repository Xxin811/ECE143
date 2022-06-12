import math
import numpy as np
import random
from itertools import combinations
def est_prob(n: int, m: int, niter: int = 100) -> float:
    '''
    :param n: num sides in regular polygon (n>=4)
    :type n: int
    :param m: num vertices for inscribed polygon (m>=3)
    :type m: int
    :param niter: num iterations for simulation
    :type m: int
    '''
    assert isinstance(n, int) and n >=4
    assert isinstance(m, int) and m >=3
    assert isinstance(niter, int)
    assert m < n
    no_repeat = 0
    for i in range(niter):
        v = random.choices(range(n),k = m)
        if len(set(v)) == len(v):
            no_repeat += 1
    p = float(no_repeat/niter)
    return p



def get_prob_shape(n: int, m: int, equilateral: bool = False) -> float:
    '''
    :param n: num sides in regular polygon (n>=4)
    :type n: int
    :param m: num vertices for inscribed polygon (m>=3)
    :type m: int
    '''
    assert isinstance(n, int) and n>=4
    assert isinstance(m, int) and m>=3
    assert isinstance(equilateral, bool)
    assert m < n

    deno = list(combinations(list(range(n)),m))
    com_len = len(deno)
    d = com_len * math.factorial(m) / (n ** m)

    if not equilateral:
        return float(d)

    elif equilateral:
        if n % m != 0:
            return float(0)
        else:
            return float(d*(n/m)/com_len)


# m = 4
# n = 8
# niter = 100
# print(est_prob(n,m,niter))
# print(get_prob_shape(n,m,True))