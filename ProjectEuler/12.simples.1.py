import math
primes = 0
triangle = 0
nat_number = 0

while primes < 500:
    nat_number += 1
    triangle = triangle+nat_number
    primes = 0
    upper_bound = int(round(math.sqrt(triangle)))
    for j in range(1,upper_bound):
        if triangle % j == 0:
            primes += 1
    primes = 2*primes

print(primes,triangle)
