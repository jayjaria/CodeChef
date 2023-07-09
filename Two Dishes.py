# cook your dish here
n=int(input())

for i in range(n):
    N,A,B,C = [int(x) for x in input().split()]
    
    if B>=N and (A+C)>=N:
        print('YES')
    else:
        print('NO')