#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#33522128640

def mult1to20():
    x = 20
    while True:
        x +=20
        y = 0
        for i in range(1,21,1):
            if x%i != 0:break
            else:y +=1
            if y ==20:return x

print(mult1to20())
