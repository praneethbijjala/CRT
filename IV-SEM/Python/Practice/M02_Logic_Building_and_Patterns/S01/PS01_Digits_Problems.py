'''
Docstring for IV-SEM.Python.Practice.M02_Logic_Building_and_Patterns.S01.PS01_Digits_Problems
sample input : 1234
sample output : 4

sample input : 12236
sample output : 5

n = int(input())
count=0
while n>0:
    count +=1
    n = n//10
print(count)

'''


'''
sample input : 1234
sample output : 10


sample input : 12236
sample output : 14 



n = int(input())
sum=0
while n >0:
    sum += (n % 10)
    n = n//10
print(10)

'''

'''
take input from user print only even numbers in the input

samplr input: 12345678
sample output: 8 6 4 2

n = int(input())
while n>0:
    d = n % 10
    if n % 2 ==0:
        print(d , end=" ")
    n=n//10
'''

'''
take input from user print only even in an order

sample input : 12345678
sample output : 2 4 6 8


def reverse(num):
    rev=0
    while num >0:
        rev = (rev*10) + (num % 10)
        num = num // 10
    return rev
n = reverse(int(input()))
while n>0:
    d = n % 10
    if d % 2 == 0:
        print(d,end=" ")
    n=n // 10
'''

