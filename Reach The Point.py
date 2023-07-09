n=int(input())
for i in range(n):
    x,y=[int(x) for x in input().split()]
    x=abs(x)
    y=abs(y)
    if x>y:
        if (x%2==0 and y%2==0) or (x%2!=0 and y%2!=0):
            print(2*x)
            continue
        else:
            print((2*x)+1)
            continue

    elif x==y:
        print(2*x)
        continue
    
    else:
        if (x%2==0 and y%2==0) or (x%2!=0 and y%2!=0):
            print(2*y)
            continue
        else:
            print((2*y)-1)
            continue

    