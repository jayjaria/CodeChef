# cook your dish here
n=int(input())

for i in range(n):
    l = int(input())
    arr = list(map(int,input().split()))

    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    
    m = d[arr[0]]
    for val in d.values():
        if val>m:
            m=val
        else:
            pass
    
    print(l-m)