# cook your dish here
n=int(input())
for i in range(n):
    N=int(input())
    S =input()
    
    num=[]
    plus=[]
    minus=[]
    
    for i in range(N):
        if S[i]=='+':
            plus.append(S[i])
        elif S[i]=='-':
            minus.append(S[i])
        else:
            num.append(S[i])
    num = [int(x) for x in num]
    num.sort(reverse=True)

    op=[]
    j=len(num)-1
    while(j!=-1):
        op.append(num[j])
        if j==0:
            j-=1
            continue
        if len(minus)!=0:
            op.append('-')
            minus.remove('-')
            j-=1
            continue
        elif len(plus)!=0:
            op.append('+')
            plus.remove('+')
            j-=1
            continue
        else:
            j-=1
            continue

    s=''
    k=len(op)-1
    while(k!=-1):
        s=s+(str(op[k]))
        k-=1

    print(s)