# cook your dish here
n=int(input())
for i in range(n):
    N,S = [int(x) for x in input().split()]
    
    t1=N
    t2=S-t1
    
    if t2<0:
        t1=N+t2
        t2=0
    D=t1-t2
    if D<0:
        D=D*(-1)
    print(D)