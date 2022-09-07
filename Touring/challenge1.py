from typing import List
import itertools

def findSubsets(arr, n)-> List[str]:
    #Function to find all subsets of given set.
    #Any repeated subset is considered only
    #once in the output
    print(arr,n)
    ans =[[]]
    for i in range(1,n+1):
        for j in itertools.combinations(arr,i):
            if j not in ans:
                ans.append(j)
    
    ans.sort(key=list)
    
    
    return ans

# R E A D M E
# DO NOT CHANGE the code below, we use
if __name__ == '__main__':
    line = "1 2 3"
    components = line.strip().split()
    n = len(components )
    print('[[' + '],['.join([','.join(['{:1}'.format(item) for item in row])
    for row in findSubsets(components,n)]) + ']]')
