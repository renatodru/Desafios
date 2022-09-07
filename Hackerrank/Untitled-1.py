t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fibs = [1,2]
    while fibs[-1]<n:
        fibs.append(fibs[-2]+fibs[-1])
    print(fibs)
    