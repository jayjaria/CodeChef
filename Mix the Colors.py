# cook your dish here
n=int(input())

for i in range(n):
    N = int(input())
    arr = list(map(int,input().split()))

    d={}
    for i in range(len(arr)):
        if arr[i] in d:
            d[arr[i]]+=1
        else:
            d[arr[i]]=1

    s = sum(list(d.values()))

    print(s-len(d))