T=int(input())
t=0
while(t<T):
    i=input().split()
    X=int(i[0])
    Y=int(i[1])
    A=int(i[2])
    B=int(i[3])
    K=int(i[4])
    
    X=X+A*K
    Y=Y+B*K
    
    if X<Y:
        print("PETROL")
    elif X>Y:
        print("DIESEL")
    else:
        print("SAME PRICE")
    t+=1