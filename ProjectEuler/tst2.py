import time
from concurrent.futures import ProcessPoolExecutor, as_completed

def checa_primo(numero):
    if numero == 2:return True
    if not numero % 2:return False
    raiz = numero ** 0.5
    if raiz == int(raiz):return False
    for i in range(3, int(raiz + 1), 2):
    #for i in range(2, numero):
        if not numero % i:return False
    return True

def checa_intervalo(inicio, tamanho):
    return sum(int(checa_primo(numero)) for numero in range(inicio, inicio + tamanho))

def ePrimo(limite, intervalo=100):
    primos = 0
    processos  = ProcessPoolExecutor(4)
    checagens = set()
    for numero in range(2,limite + 1, intervalo):
        final = min(limite - numero, intervalo)
        checagens.add(processos.submit(checa_intervalo, numero, final))
    for checagem in as_completed(checagens):
        primos += checagem.result()
    return primos

def teste():
    for intervalo in (4, 10, 50, 100, 1000, 5000, 10000):
        tic = time.time()
        primos = ePrimo(100000, intervalo)
        toc = time.time()

        print("\n Agrupando {} números por tarefa:".format(intervalo))
        print("total de números primos no intervalo definido = "+ str(primos))
        print("tempo gasto para processar = " + str(toc-tic)+"s")

if __name__ == "__main__":
    teste()