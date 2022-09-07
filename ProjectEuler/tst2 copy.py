import time
from concurrent.futures import ProcessPoolExecutor, as_completed

def ndiv(numero):
    cont = 1    
    for div in range(1,1 + numero//2):
        if numero % div == 0:cont += 1
    if cont >=500: return True
    else: return False

def ediv(limite, intervalo=100):
    primos = 0
    processos = ProcessPoolExecutor(4)
    checagens = set()
    for numero in range(2,limite + 1, intervalo):
        final = min(limite - numero, intervalo)
        checagens.add(processos.submit(checa_intervalo, numero, final))
    for checagem in as_completed(checagens):
        primos += checagem.result()
    return primos

def teste():    
    number = 0
    cont = 1
    result = 0
    resultdiv = 0
    while True:
        number = number + cont    
        cont += 1
    
        resultdiv = ndiv(number)
        if resultdiv > result:
            print(number,"--",resultdiv)
            result = resultdiv
    
    
    
    for intervalo in (4, 10, 50, 100, 1000, 5000, 10000):
        tic = time.time()
        primos = ePrimo(100000, intervalo)
        toc = time.time()


if __name__ == "__main__":
    teste()
    

    
 