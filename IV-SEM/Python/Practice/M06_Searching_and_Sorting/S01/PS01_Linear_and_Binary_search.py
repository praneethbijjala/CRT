'''
def Linear_search(nums,target):
    for i in range(len(nums)):
        if nums[i]== target:
            return 1
    return -1

li= list(map(int,input().split()))
target1=int(input())


print(Linear_search(li,target1))

target2=int(input())
print(Linear_search(li,target2))


print(Linear_search([12,15,45,67,89,20],15))#1
print(Linear_search([12,15,45,67,89,20],100))#-1 
'''


def Binary_search(nums,target):
    low,high = 0,len(nums)-1
    while low < high:
        mid =(low + high) //2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid -1
        else:
            low = mid+1
    return -1
li = list(map(int,input().split()))
target=int(input())

print(Binary_search(li,target))