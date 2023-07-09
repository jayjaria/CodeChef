# cook your dish here
n =int(input())

for i in range(n):
    A,B,X=[int(x) for x in input().split()]
    years = (B-A)/X
    print(int(years))