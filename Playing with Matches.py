sticks ={'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}

n = int(input())
for i in range(n):
    A,B = [int(x) for x in input().split()]
    S = A+B
    D = str(S)
    c=0
    for i in D:
        c=c+sticks[i]
    print(c)