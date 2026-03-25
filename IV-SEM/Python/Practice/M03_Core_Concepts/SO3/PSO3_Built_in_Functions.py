"""
#1) Find Largest Number (using max())
#input:[12,78,32,54,69,100]
#output:100

li=[12,78,32,54,69,100]
max_num=li[0]
for ele in li:
    if ele > max_num:
        max_num=ele
print(max_num)

"""
"""
#Check palidrome(using reversed() & join())
s=input()
print("Palidrome" if s == s[::-1] else "not palindrome")
print("".join(reversed([1,2,3,4,5])))
print(list(reversed))
"""
"""
#Index with value (Using enumerate)
li=['preeti','mujeeb','kalyani','dinesh','suresh']
for index,value in enumerate(li):
    print(index,"==>",value)
"""

li1=[1,2,3,4,5]
li2=[10,20,30,40,50]
#res=[11,22,33,44,55]
