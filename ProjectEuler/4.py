lista=[]
for i in range(100,1000):
    for n in range(100,1000):
        x = str(i*n)
        if x==x[::-1] and len(x)==6:
            lista.append(x)
            print(x)
            print(max(lista))
            