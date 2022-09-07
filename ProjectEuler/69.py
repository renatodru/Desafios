#Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.



def rel_prime(n):
    cont = 1
    if n%2==0:
        for i in range(3,n,2):
            pass
    else:
        for i in range(2,n):
            if n%i != 0:
                cont += 1
    
    
    return cont



for n in range(2,1+10):
    print(n,rel_prime(n))

# build a list of values
