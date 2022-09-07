import math
import numpy as np
import itertools


def generate_vectors(n_length) -> np.ndarray:
    lst = list(map(list, itertools.product([0, 1], repeat=n_length - 1)))
    binary_lists = [l + [1] for l in lst]
    for bin_list in binary_lists:
        for i in range(n_length - 1, -1, -1):
            if bool(bin_list[i]):
                continue
            bin_list[i] = bin_list[i + 1] * 10
    return np.asmatrix(binary_lists).transpose()


all_matrices = []
for i in range(1, 14):
    all_matrices += [generate_vectors(i)]


def is_s(n, sqrt_n, all_matrics):
    numbers = [int(x) for x in list(str(n))]
    vecs = all_matrics[len(numbers) - 1]
    return sqrt_n in np.array(numbers) * vecs


MAX = 10**12
sqrtmax = math.sqrt(MAX)
sum_of_s = 0

for i in range(2, int(sqrtmax + 1)):
    if i % 10000 == 0:
        print(i/sqrtmax)
    if is_s(i * i, i, all_matrices):
        sum_of_s += i ** 2

print(sum_of_s)