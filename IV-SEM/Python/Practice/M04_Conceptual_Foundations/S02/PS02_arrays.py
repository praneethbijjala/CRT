'''
#input:[12,45,36,78,96]
#output:[96,78,36,45,12]

li=[12,45,36,78,96]
res=[]
stop= -1* (len(li)+1)
for i in range(-1,stop,-1):
    res.append(li[i])
print(res)
#List comprehension
res1=[li[i] for i in range(-1,stop,-1)]
print(res1)

li=[12,45,36,78,96]
n=len(li)
for i in range(n//2):
        li[i],li[n-i-1]=li[n-i-1],li[i]
print(li)

li=[12,45,36,78,96]
res=[]
for ele in li:
    #res.insert(0,ele)
    res=[ele]+res
print(res)

def  check_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            return False
    return True
nums=[12,36,45,55,69,100]
print(check_sorted(nums))
'''
li=[1,2,3,4,1,2,5,2,4]
res = {}
for ele in li:
    if ele not in res:
        res[ele]=1
        