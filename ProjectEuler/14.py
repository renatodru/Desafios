def collatz(x):
    contx = 1
    while x > 1:
        if x % 2 == 0:x /= 2
        else:x = 3*x+1
        contx += 1
    return contx

maiorcoll = 0
maionum = 0
for i in range(1000000):
    x = collatz(i)
    if x>maiorcoll:
        maiorcoll,maiornum = x,i
        print(maiorcoll,maiornum)
print(maiorcoll,maiornum)