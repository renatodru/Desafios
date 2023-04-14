import timeit

def soe1(n):
    primes = [True for i in range(n+1)]
    primes[0], primes[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    prime_list = []
    for i in range(n+1):
        if primes[i]:
            prime_list.append(i)    
    return prime_list

def soe2(n):   
    primes = set(range(2, n+1))
    for i in range(2, int(n**0.5)+1):
        if i in primes:
            multiples = range(i*i, n+1, i)
            primes.difference_update(multiples)
    return sorted(primes)

def soe3(n):
    sieve = [True] * (n+1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i in range(n+1) if sieve[i]]

def soe4(n):
    primes = set(range(2, n+1))
    for i in range(2, int(n**0.5)+1):
        if i in primes:
            primes -= set(range(i*i, n+1, i))
    return sorted(primes)

def soe5(n):
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            primes[i*i:n+1:i] = [False] * len(primes[i*i:n+1:i])
    return [i for i in range(n+1) if primes[i]]

def soe6(n):
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False

    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    
    return [i for i in range(n+1) if primes[i]]

def soe7(n):
    primes = bytearray(b'\x01' * (n+1))
    primes[0], primes[1] = False, False
    for i in range(3, int(n**0.5)+1, 2):
        if primes[i]:
            primes[i*i:n+1:i] = bytearray(b'\x00' * len(primes[i*i:n+1:i]))
    return [2] + [i for i in range(3, n+1, 2) if primes[i]]

def soe8(n):
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False
    for i in range(3, int(n**0.5)+1, 2):
        if primes[i]:
            primes[i*i::2*i] = [False] * ((n-i*i)//(2*i) + 1)
    return [2] + [i for i in range(3, n+1, 2) if primes[i]]



import numpy as np

def soe10(n):
    primes = np.ones(n+1, dtype=bool)
    primes[0:2] = False
    primes[4::2] = False
    for i in range(3, int(n**0.5)+1, 2):
        if primes[i]:
            primes[i*i::2*i] = False
    return np.concatenate(([2], np.nonzero(primes[3:n+1:2])[0] + 3))



tempo = timeit.timeit('soe7(10**4)', setup='from __main__ import soe7', number=100)
print('Tempo de execução:', tempo)

tempo = timeit.timeit('soe8(10**4)', setup='from __main__ import soe8', number=100)
print('Tempo de execução:', tempo)

tempo = timeit.timeit('soe10(10**4)', setup='from __main__ import soe10', number=100)
print('Tempo de execução:', tempo)
