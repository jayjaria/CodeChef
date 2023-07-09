n=int(input())
import math

for i in range(n):
    N=int(input())
    
    D = 1+8*N 
    s = (-1+math.sqrt(D))/2

    print(math.floor(s))