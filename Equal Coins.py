T=int(input())

t=0
while(t<T):
    i=input().split()
    X=int(i[0])
    Y=int(i[1])
    
    value=X+Y*2
    
    if X+Y==1 or X+Y==0:
        print("no")
    
    elif X==0 and Y%2!=0:
        print("no")
    elif value%2==0:
        print("yes")
    else:
        print("no")
    t+=1