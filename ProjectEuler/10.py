
def primo(num):
    cont = 5
    soma = 10
    while cont+2<num:
        cont += 2
        if str(cont)[-1]=="5": continue
        if verprimo(cont):
            soma += cont
        if cont%1001 == 0:print(cont)

    print(cont,soma)

def verprimo(i):
    for n in range(3,(i//3)+1,2):
        if i%n == 0:return False
    return True
    

primo(2000000)
        