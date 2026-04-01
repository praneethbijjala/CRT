'''1. Square Star Pattern
n=4
Output:
* * * *
* * * *
* * * *
* * * *

n = int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

2. Right Angle Triangle
n=4
Output:
*
* *
* * *
* * * *

n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

3. Inverted Triangle
n=4
Output:
* * * *
* * *
* *
*
'''
n = int(input())
for i in range(n):
    for j in range(n-i,0,-1):
        print("*",end=" ")
    print()
