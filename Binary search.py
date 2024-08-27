# Binary search
l= [1,2,3,4,5,6,7]
low = 0
high = len(l)-1
user = 7
while(low<=high):
    mid = (low + high)//2
    if user>l[mid]:
        low = mid +1
    elif user <l[mid]:
        high = mid -1
    elif user == l[mid]:
        print(mid)
        break
    else:
        print(-1)
