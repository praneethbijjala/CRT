#Digital root sum
#386 ==> 17 ==> 8
def Digital_sum(n):
     if n<=9:
         return n
     s=sum([int(ch) for ch in str(n)])
     return Digital_sum(s)
print(Digital_sum(386))#8

#Sorted Check
