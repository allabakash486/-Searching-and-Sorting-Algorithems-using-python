#Quick Sort method
L= [1,2,3,4,5,6,7,0,9,8,7,6,5,4,3,2,1,0]
def Quick(L):
    if len(L)<=1:
        return L
    pivot = L[0]
    low = [ L[i] for i in range(1,len(L)) if pivot>L[i]]
    high = [L[i] for i in range(1,len(L)) if pivot<=L[i]]
    return Quick(low)+[pivot]+Quick(high)
print(Quick(L))
        
        
