'''
Docstring for IV-SEM.Python.Practice.M02_Logic_Building_and_Patterns.S02.PS02_FFactors&Primes
 
Print all the factors of the given numbers

input : 12
output: 1 2 3 4  6 12


n=int(input("Enter a number: "))
count=0
for i in range(1,n+1):
    if n % i == 0:
        count +=1
print(count)

'''

'''

Check whether given number prime or not

input : 7
 output: prime

 input: 9
 output : Notprime
 


n=int(input("Enter a number: "))
count=0
for i in range(2,n//2+1):
    if n % i ==0:
        count +=1
if count ==0:
    print("Prime")
else:
    print("Not Prime")

    '''


'''
print all the prime numbers in the given range

input: 1 10
output: 2 5 7

'''
'''

'''
n=int(input())
fact=1
for i in range(1,n+1):
    fact= fact *1
print(fact)