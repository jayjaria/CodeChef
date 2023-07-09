n=int(input())

for i in range(n):
    N,K = [int(x) for x in input().split()]
    arr = list(map(int,input().split()))

    d={}
    d['E']=0
    d['O']=0
    for i in arr:
        if i%2==0:
            d['E']+=1
        else:
            d['O']=1

    if K==0:
        if d['E']<N:
            print('YES')
        else:
            print('NO')
        continue
    elif d['E']>=K:
        print('YES')
        continue
    else:
        print('NO')