# cook your dish here
n =int(input())

for i in range(n):
    D,L,R = [int(x) for x in input().split()]
    if D>=L and D<=R:
        print('Take second dose now')
    elif D<L:
        print('Too Early')
    else:
        print('Too Late')