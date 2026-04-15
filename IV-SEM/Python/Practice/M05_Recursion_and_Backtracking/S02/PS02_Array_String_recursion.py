#sum of array elements

def Array_sum (nums):
    s=0
    for i in range(len(nums)):
        s+= nums[i]
    return s
print(Array_sum([1,2,3,4,5]))#15

#Recursive Approach
def Array_sum1(nums,index):
    if index ==-1:
        return 0
    return nums[index]+ Array_sum1(nums,index-1)
print(Array_sum1([1,2,3,4,5],4))#15

def Array_sum2(nums):
    if len(nums)==0:
        return 0
    return nums[-1] + Array_sum2(nums[:-1])
print(Array_sum2((1,2,3,4,5)))



def Recurse_String(st):
    if len(st)==0:
        return ""
    return st[-1] +Recurse_String(st[:-1])
print(Recurse_String("abc"))#"cba"