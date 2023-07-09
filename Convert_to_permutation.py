t=int(input())
i=0
while i<t:
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    d=[]
    j=1
    while j<=n:
        d.append(j)
        j+=1
    a.sort()
    k=0
    while k<len(d):
        if d[k]==a[k]:
            pass
        elif a[k]<d[k]:
            c+=d[k]-a[k]
        else:
            c=(-1)
            break

        k+=1
    print(c)
    i+=1
        
            
            
        
        
        
        
        
        
    