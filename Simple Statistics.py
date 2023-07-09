n=int(input())
for i in range(n):
    N,K=[int(x) for x in input().split()]
    A = list(map(int,input().split()))

    A.sort()
    s=0
    for j in range(K,N-K):
        s=s+A[j]
    avg = s/(N-2*K)

    print(format(avg, '.6f'))