# cook your dish here
n=int(input())
for i in range(n):
    N=int(input())
    A = list(map(int,input().split()))

    arr = [1,2,3,4,5,6,7]
    c=0
    p=0
    while(c<7):
        if A[p] in arr:
            c+=1
            p+=1
        else:
            p+=1

    print(p)