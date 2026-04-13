'''
def Natural_sum(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s

print(Natural_sum(5))
print(Natural_sum(10))

# Recursion
def Natural_sum1(n):
    if n == 1:
        return 1
    else:
        return n + Natural_sum1(n-1)
print(Natural_sum1(5))
print(Natural_sum1(10))
 
'''

#Find factorial of a number
#Traditional Approch
def factorial(n):
    f=1
    for i in range(n,0,-1):
        f *=i
    return f
print(factorial(5))#120
print(factorial(3))#6
