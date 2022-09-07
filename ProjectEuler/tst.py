
print(__name__=='__main__')


def verprimo(i):
    for n in range(3,(i//3)+1,2):
        print(n)
        if(n%2==0):print("par")

def start():
    for x in range(3,100):
        verprimo(x)