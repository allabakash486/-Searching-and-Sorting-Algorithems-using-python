# Selection sorting method
l = [1,0,9,8,7,6,5,4,3,2,1,-1,-2,-3,-4,-4]
def Selection_sort(l):
    for val in range(len(l)-1):
        low= val
        for ind in range(val+1,len(l)):
            if l[low]>l[ind]:
                low = ind
        l[low],l[val]=l[val],l[low]
    return l
print(Selection_sort(l))
