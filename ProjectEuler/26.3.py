import labmath
import time

def main():
    start_time = time.time()
    lenght = 0
    ret = 0
    for x in range(100, 100000):
        if labmath.isprime_nm1(x, fac=None) == True:
            if labmath.multord(10, x) > lenght :
                lenght = labmath.multord(10, x)
                ret = x
    print("result is :", ret, " in : ",time.time() - start_time, "seconds")

main()