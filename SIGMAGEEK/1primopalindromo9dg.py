import math
import numpy

def is_prime(n):
    if n%5==0:return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def gera_primos_21dg():
    primos1 =[]
    
    for i in range(100_000_000_000_000_000_001, 199_999_999_999_999_999_999,2):
        if str(i) == str(i)[::-1] and is_prime(i):
            primos1.append(i)
    print("Primos 1x10E21 gerados")
    
    primos3 =[]
    for i in range(300_000_000_000_000_000_001, 399_999_999_999_999_999_999,2):
        if str(i) == str(i)[::-1] and is_prime(i):
            primos3.append(i)
    print("Primos 3x10E21 gerados")
    
    primos7 =[]
    for i in range(700_000_000_000_000_000_001, 799_999_999_999_999_999_999,2):
        if str(i) == str(i)[::-1] and is_prime(i):
            primos7.append(i)
    print("Primos 7x10E21 gerados")
    
    primos9 =[]
    for i in range(900_000_000_000_000_000_001, 999_999_999_999_999_999_999,2):
        if str(i) == str(i)[::-1] and is_prime(i):
            primos9.append(i)
    print("Primos 9x10E21 gerados")
    
    return primos1+primos3+primos7+primos9

indice = []
for x in range(len(pi)):
    try:
        teste = pi[x:x+9]
    except:break
    else:
        if teste == teste[::-1]:
            if int(teste) in primos:
                indice.append([x,teste])
print(indice)

#[[129078, '318272813'], [247146, '134888431'], [268797, '961212169'], [638700, '111262111']]