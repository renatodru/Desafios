from timeit import default_timer as timer


from numba import njit, prange


@njit
def split_match(a, b):
    if a == b:
        return True
    if a < b:
        return False
    mod = 10
    while mod < a:
        if split_match(a // mod, b - a % mod):
            return True
        mod *= 10
    return False


@njit(parallel=True)
def solve(power):
    n = 10 ** power
    total = 0
    for x in prange(4, int(n ** 0.5 + 1)):
        if x % 9 <= 1 and split_match(x ** 2, x):
            total += x ** 2
    return total
  
print(solve(12))