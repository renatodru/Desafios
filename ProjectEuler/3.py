from datetime import datetime

def primo(num):
    primos = []
    for i in range((num//3),3,-2):
        if str(i)[-1]=="5": continue
        if verprimo(i):
            primos.append(i)
            print(i)
    primosval=[]
    for primo in primos:
        if num%primo == 0:
            primosval.append(primo)
    return primosval

def verprimo(i):
    for n in range(3,(i//3)+1,2):
        if(n%2==0):
            print("ERRO")
            return False
        if i%n == 0:return False
    return i
    
#x = 600851475143
#x = 13195
#x = 60
for x in range(100):
    print(primo(x))

        
