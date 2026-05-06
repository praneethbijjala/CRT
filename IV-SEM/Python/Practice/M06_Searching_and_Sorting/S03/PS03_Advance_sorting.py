def Merge(left,right):
    i,j=0,0
    res=[]
    while i< len(left) and j <len(right):
        if left[i] <=right[j]:
            res.apprnd(left[i])
            i +=1
        else:
            res.append(right[j])
            j +=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res