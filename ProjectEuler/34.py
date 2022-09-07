#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#Note: As 1! = 1 and 2! = 2 are not sums they are not included.

def fact(num):
    multi = 1
    for x in range(1,num+1):
        multi *= x
    return multi


achados = []

for i in range(3,1+10**8):
    somaprodfact = 1
    if sum([fact(int(z)) for z in str(i)])==i:achados.append(i)
    
print(achados)