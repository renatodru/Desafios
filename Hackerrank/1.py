x = 1
y = 1
z = 1
n = 2



from itertools import combinations

from pandas import concat

if __name__ == '__main__':
    #x = int(input())
    #y = int(input())
    #z = int(input())
    #n = int(input())
    
    print([[int(a[0]),int(a[1]),int(a[2])] for a in [str(i) + str(j) +str(k) for i in range(x+1) for j in range(y+1)for k in range(z+1) if i+j+k != n]])

    print("[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]")