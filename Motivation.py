n=int(input())

for i in range(n):
    arr=[]
    N,X = [int(x) for x in input().split()]
    for j in range(N):
        S,R = [int(y) for y in input().split()]
        if S<=X:
            arr.append(R)
    print(max(arr))