l= [1,2,3,4,5,6,7]
low = 0
high = len(l)-1
user = 7
while(low<=high)and (l[low]<=user<l[high]):
    ind = int(low + ((low-high)/(l[low]-l[high])))*(user-l[low])
    if user>l[ind]:
        low = ind +1
    elif user <l[ind]:
        high = ind -1
    elif user == l[ind]:
        print(ind)
        break
    else:
        print(-1)
