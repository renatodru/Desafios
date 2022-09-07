#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
# which means that 28 is a perfect number.

#A number n is called deficient if the sum of its proper divisors is less than n and it
# is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number
# that can be written as the sum of two abundant numbers is 24. By mathematical analysis,
# it can be shown that all integers greater than 28123 can be written as the sum of two
# abundant numbers. However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be expressed as the sum
# of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two
# abundant numbers. #4179871

from math import sqrt
from itertools import compress

def ldivisores(num):
    ldiv = []
    for div in range(1,1+num//2):
        if num%div == 0:ldiv.append(div)
    return ldiv

def n_abundante(numero):
    if sum(ldivisores(numero))>numero:return True
    else:return False


def int_dif_2abu(numero,l_abundantes):
    l_abund_m_n = [num for num in l_abundantes if num < numero + 1]
    tam = 3 + len(l_abund_m_n)//2
    for abund_m in l_abund_m_n[0:tam]:
        for abund_M in l_abund_m_n[tam::-1]:
            if abund_m + abund_M == numero:return False
    return True
  

abundant_nos = [numero for numero in range(1,28124) if n_abundante(numero)]

num_list = [True]*28123
k = 0
for i in abundant_nos:
    for j in abundant_nos[k:]:
        if(i+j>28123): break
        num_list[i+j-1] = False
    k+=1
answer = sum(compress(range(1,28124),num_list))

print(answer, answer==4179871)