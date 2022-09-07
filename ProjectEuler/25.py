
f,a = 1,1
cont = 2
while len(str(f))<1000:
    f,a = f + a,f
    cont +=1
    print("Digitos",len(str(f)),"termo: ",cont," = ",f)


