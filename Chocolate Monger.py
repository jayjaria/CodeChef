# cook your dish here
n=int(input())
for i in range(n):
    n,x=[int(x) for x in input().split()]
    A = list(map(int,input().split()))

    d={}
    for j in range(len(A)):
        if A[j] in d:
            d[A[j]]+=1
        else:
            d[A[j]]=1
    
    for key,val in d.items():
        d[key]=val-1

    value_sum=sum(d.values())
    if value_sum<x:
        print(len(d)-(x-value_sum))
    else:
        print(len(d))