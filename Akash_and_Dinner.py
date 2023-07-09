n=int(input())

for i in range(n):
    N,K = [int(x) for x in input().split()]
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    
    d={}
    for j in range(N):
        if A[j] in d and d[A[j]]>B[j]:
            d[A[j]] = B[j]
        elif A[j] not in d:
            d[A[j]] = B[j]
        else:
            pass
    if(len(d)>=K):
        arr=list(d.values())
        arr.sort()
        min_time=0
        for k in range(K):
            min_time+=arr[k]
        print(min_time)
    else:
        print('-1')