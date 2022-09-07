from math import sqrt
from itertools import count
from collections import defaultdict
# Sieve of Eratosthenes
# Modified from the Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/


def prime_candidates(begin=5, end=None):
    """Returns all prime candidates between begin and end(>=begin and <end). If end is None, it behaves like end = infinity. A prime candidate is either 2, 3 or a number of the form 6k-1 or 6k+1. 
    """
    cur = begin
    if cur % 2 == 0:
        if cur == 2:
            yield 2
        cur += 1
    if cur % 6 == 3:
        if cur == 3:
            yield 3
        cur += 2
    elif cur % 6 == 1:
        yield cur
        cur += 4
    gen = count(cur, step=6) if not end else xrange(cur, end, 6)
    for n in gen:
        yield n
        yield n + 2


def gen_primes(mx=100000000000000):
    """ Generate all prime numbers (strictly) below mx
    """
    mx_sqrt = int(sqrt(mx)) + 1
    D = {}
    yield 2
    yield 3
    for q in prime_candidates():
        if q >= mx:
            return
        if q not in D:
            yield q
            if q < mx_sqrt:
                D[q * q] = [q]
        else:
            for p in D[q]:
                qp = q + p
                while qp % 6 not in [1, 5]:
                    qp += p
                if qp < mx:
                    D.setdefault(qp, []).append(p)
            del D[q]


def factorize(n):
    """Returns factorization of n as a dictionary. If n is prime, returns None. Keys are the primes,
    corresponding values are their powers in the factorization.
    So a return value of {a:b, c:d} means n = (a^b)*(c^d) with a, c primes. 
    """
    res = defaultdict(lambda: 0)
    for p in gen_primes(mx=n):
        while n % p == 0:
            n = n // p
            res[p] += 1
        if n == 1:
            return dict(res)

if __name__ == '__main__':
    number = 0
    cont = 1

    ndiv = 0

    while True:
        number += cont        
        qntdiv = 1
        for i,j in factorize(number).items():qntdiv *= (j+1)
        if qntdiv > ndiv:
            ndiv = qntdiv
            print(number," - ",ndiv)
        cont += 1