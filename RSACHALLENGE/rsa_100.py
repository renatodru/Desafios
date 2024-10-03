import math
import sympy
import datetime

def busca(arvore,valor):
    esquerda = arvore[0]
    direita = arvore[-1]
    centro = (esquerda+direita)//2
    ver_centro = centro
    while centro!=valor:
        if valor<centro:
            direita,centro = centro,(esquerda+centro)//2
            ver_centro = centro
        elif centro<valor:
            esquerda,centro = centro,(centro+direita)//2
            ver_centro = centro
        if ver_centro==centro:            
            return centro
    return centro

def _test_busca():
    for teste in range(1000):
        inicio=datetime.datetime.now()
        valor = 39020571855401265608465770302117235537201395138561
        lista = list(range(37975227936943673922808872755445627854565536638199,40094690950920881030683735292761468389214899724061,(40094690950920881030683735292761468389214899724061-37975227936943673922808872755445627854565536638199)//10))
        print(len(lista))
        busca(lista,valor)
        print(teste,"--tempo: ",datetime.datetime.now()-inicio)


def procura(rsa):
    print(math.floor(math.sqrt(rsa)))
    print(math.ceil(math.sqrt(rsa)))
    print(int(math.sqrt(rsa)))
    
    rsa_int_raiz = math.floor(math.sqrt(rsa))
    rsa_resto_raiz = rsa % rsa_int_raiz
    resto = rsa_resto_raiz
    
    esquerda = rsa_int_raiz - rsa_resto_raiz
    direita = rsa_int_raiz    
    centro = (esquerda+direita)//2
    print(esquerda)
    print(centro)
    print(direita)
    while resto!=0:
        break

        


RSA100 =            1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
RSA_100_1 =         37975227936943673922808872755445627854565536638199
RSA_100_2 =         40094690950920881030683735292761468389214899724061
RSA100_05INT_sup =  39020571855401265608465770302117235537201395138560 # math.ceil(math.sqrt(RSA100)))

#raio da circunferencia = 1359030140443632694001585195237547736033402118515563.005820104519181817864928059057946108302473788291885614080047088126336328669427837428384137632511465531737214689

RSA100_05INT_REST = 23209278125864873499065245402229085800855536294139 # RSA100 % RSA100_05INT)
#raiz = Decimal(rsa**0.5) #from decimal import Decimal
if __name__=="__main__":
    procura(RSA100)

# inicio = datetime.datetime.now()

# print(sympy.isprime(RSA_100_2))
# print(sympy.isprime(RSA_100_1))
# print(sympy.isprime(RSA100))
# print(RSA_100_1*RSA_100_2==RSA100)
#print('{:.20f}'.format(sqrt(RSA100)))

# print("tempo: {}".format(datetime.datetime.now() - inicio))


