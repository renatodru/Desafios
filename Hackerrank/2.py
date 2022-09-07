if __name__ == '__main__':
    cases = int(input())

    for i in range(cases):
        tamA,A,tamB,B = input(),set(input().split()),input(),set(input().split())     
        print(A.issubset(B))