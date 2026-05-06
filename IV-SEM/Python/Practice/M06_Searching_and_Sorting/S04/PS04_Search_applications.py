def Lower_bound(arr,target):
    low,high=0,len(arr)-1
    while low <=high:
        mid = (low + high)//2
        if target > arr[mid]:
            low = mid+1
        else:
            high = mid-1
    return low

print(Lower_bound([2, 3, 7, 10, 11, 11, 25],9))#3
print(Lower_bound([2, 3, 7, 10, 11, 11, 25],11))#4
print(Lower_bound([2, 3, 7, 10, 11, 11, 25],100))#7