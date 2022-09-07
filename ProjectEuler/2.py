


n = 1000
fibs = [0,1]
while fibs[-1]<n:
    fibs.append(fibs[-2]+fibs[-1])
print(sum([x for x in fibs[:-1] if x%2==0]))