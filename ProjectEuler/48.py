#The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

#Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.

soma = 0

for i in range(1,1001):
    soma = soma + i**i
    if i%25 == 0:print(i,soma)
print(str(soma)[-10:])