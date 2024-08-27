#Sorting Methods :
# Bubble Sort method
L=[1,2,1,2,1,3,0,-1,-2,-3,4,9,3,4,5,6]
def Bouble_sort(L):
    for val in range(len(L)-1,0,-1):
        for ind in range(val):
            if L[ind]>L[ind+1]:
                L[ind],L[ind+1]=L[ind+1],L[ind]
    return L
print(Bouble_sort(L))
