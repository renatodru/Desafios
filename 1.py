#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def mult(numero,lista):
    soma = 0   
    for i in range(1,numero):
            if i%lista[0]==0 or i%lista[1]==0:
                soma += i
    print(soma)



numero = 1000
lista = [3,5]

mult(numero,lista)