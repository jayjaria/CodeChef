# cook your dish here
n=int(input())

for i in range(n):
    a,b,c,d,K =[int(x) for x in input().split()]
    min = abs(a-c)+abs(b-d)

    if min>K:
        print('NO')
    elif min==K:
        print('YES')
    else:
        if (K- min)%2==0:
            print('YES')
        else:
            print("NO")
            