# cook your dish here
n=int(input())
for i in range(n):
    N,W = [int(x) for x in input().split()]
    arr = list(map(int,input().split()))

    arr.sort()
    index=N-1
    m=max(arr)
    j=1
    while(m<W):
        arr.pop(index)
        j+=1
        m+=max(arr)
        index-=1
    holidays=N-j
    print(holidays)