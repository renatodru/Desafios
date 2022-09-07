
def primo(num):
    primos = 1
    cont = 2
    while primos<num:
        cont += 2
        if str(cont)[-1]=="5": continue
        if verprimo(cont):
            primos += 1
            print("primo nº",primos," = ",cont)


def verprimo(i):
    for n in range(3,(i//3)+1,2):
        if i%n == 0:return False
    return i
    

primo(10002)
        
