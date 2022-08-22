import datetime

import sympy

print()

def gera_primos_21dg():
    primos =[]
    extrem = [1,3,7,9]
    x = 0
    for ex in extrem:
        for center in range (0,10):
            inicio = datetime.datetime.now()
            print("iniciando {}".format(inicio))
            for laterall in range(0, 999_999_999):
                lateral = str(laterall).zfill(9)
                teste = int(str(ex)+lateral[::-1]+str(center)+lateral+str(ex))                
                if sympy.isprime(teste):
                    primos.append(teste)
                    if len(primos)%50000 == 0:
                        print("Qnt calculada: ",len(primos)," - tempo: ",datetime.datetime.now()-inicio,len(primos)," último calculado: ",teste," lateral: ",laterall," percent ",laterall/999_999_999*100)
                        x +=1
                        if x==10:return None
    #         print("proximo loop central ",datetime.datetime.now()-inicio,len(primos))
    # return primos

gera_primos_21dg()