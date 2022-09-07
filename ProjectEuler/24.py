#A permutation is an ordered arrangement of objects. For example, 3124
# is one possible permutation of the digits 1, 2, 3 and 4. If all of
# the permutations are listed numerically or alphabetically, we
# call it lexicographic order. The lexicographic permutations of
# 0, 1 and 2 are:
#'012   021   102   120   201   210
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def main():
    lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    texto = ['']*10
    cont = 0

    for a in lista:
        texto[0] = a
        for b in lista:
            if len(list(set(a+b)))==2:
                texto[1] = b
                for c in lista:
                    if len(list(set(a+b+c)))==3:
                        texto[2] = c
                        for d in lista:
                            if len(list(set(a+b+c+d)))==4:
                                texto[3] = d
                                for e in lista:
                                    if len(list(set(a+b+c+d+e)))==5:
                                        texto[4] =e
                                        for f in lista:
                                            if len(list(set(a+b+c+d+e+f)))==6:
                                                texto[5] = f
                                                for g in lista:
                                                    if len(list(set(a+b+c+d+e+f+g)))==7:
                                                        texto[6] = g
                                                        for h in lista:
                                                            if len(list(set(a+b+c+d+e+f+g+h)))==8:
                                                                texto[7] = h
                                                                for i in lista:
                                                                    if len(list(set(a+b+c+d+e+f+g+h+i)))==9:
                                                                        texto[8] = i
                                                                        for j in lista:
                                                                            if len(list(set(a+b+c+d+e+f+g+h+i+j)))==10:
                                                                                texto[9] = j
                                                                                cont += 1
                                                                                if cont % 10000==0:
                                                                                    print(cont,texto)
                                                                                if cont > 990000:
                                                                                    print(cont,texto)
                                                                                    if cont>1000010:
                                                                                        return

main()