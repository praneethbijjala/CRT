'''
Docstring for IV-SEM.Python.Practice.M02_Logic_Building_and_Patterns.S06.PS07_Advamce_Patterns
1. Pascal Triangle

n=5

output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

'''

n=int(input())
for i in range(n):
    num=1
    for j in range(i+1):
        print(num,end=" ")
        num= num * (i-j)//(j+1)
    print()