from math import sqrt

def divisors(number: int):
    cont, n = 0, 1
    stop = sqrt(number)
    if int(stop) == stop: cont = 1
    while n < stop:
        if number % n == 0:cont += 2
        n += 1
    return cont

def get_triangle_number(limit: int):
    n = triangle_number = 0
    while divisors(triangle_number) < limit:
        n += 1
        triangle_number += n
    return triangle_number

print(get_triangle_number(500))