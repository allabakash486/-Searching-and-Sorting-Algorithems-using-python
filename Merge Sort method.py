#Merge Sort
L = [1,2,3,4,5,66,0,9,8,7,6,5,5,4,3,3,21,1]
def Conqure(Mlist,Llist,Rlist):
    mi,ri,li=0,0,0
    while(li<len(Llist) and ri<len(Rlist)):
        if (Llist[li]>Rlist[ri]):
            Mlist[mi] = Rlist[ri]
            ri += 1
        else:
            Mlist[mi] = Llist[li]
            li += 1
        mi +=1
    while (len(Llist)>li):
        Mlist[mi] = Llist[li]
        li += 1
        mi += 1
    while (len(Rlist)>ri):
        Mlist[mi] = Rlist[ri]
        ri += 1
        mi += 1 
def Divid(L):
    if len(L)>1:
        left,right = L[:len(L)//2],L[len(L)//2:]
        Divid(left)
        Divid(right)
        Conqure(L,left,right)
Divid(L)
print(L)
    
