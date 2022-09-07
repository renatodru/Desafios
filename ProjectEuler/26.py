from decimal import *

def conta_n_l(l_numero_cortado):

    for numero_atual in l_numero_cortado:
        if l_numero_cortado.count(numero_atual):
            pass




n2 = 3+2**10
getcontext().prec = n2*2
for divisor in range(1,1000):
    numero_teste = str(Decimal(Decimal(1)/Decimal(divisor)))[4+2*(len(str(divisor))):-1]
    tam = int(len(numero_teste))
    if len(numero_teste)<n2 or numero_teste.count(numero_teste[0:tam//4])>=3:continue
    #print(len(numero_teste[0:tam//4]),numero_teste[0:tam//4],'-',len(numero_teste[tam//4:tam//2]),numero_teste[tam//4:tam//2])
    print(divisor,len(numero_teste),"-",numero_teste)
    #for tamanho in range(1,1+len(numero_teste)//2):
        #l_numero_cortado = [numero_teste[i:i+tamanho] for i in range(0,len(numero_teste),tamanho)]
            
        #print("div:",divisor,"tam corte:",tamanho,"- nº conj lista",len(l_numero_cortado),"nº rep",l_numero_cortado.count(l_numero_cortado[0]),"- lista:",l_numero_cortado[0])