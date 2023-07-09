n=int(input())
for i in range(n):
    N=int(input())

    if N==0:
        print('1')
        continue
    arr=[0]*(N+1)
    
    s = pow(2,N)
    for j in range(1,N):
        arr[j]=j
    arr[0]=1
    
    s1=0
    for k in arr:
        s1+=k
    arr[N]=s-s1
    
    print(*arr)

    