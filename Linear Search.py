#Linear search
def Linear_search(l,user):
    for val in range(len(l)):
        if user == l[val]:
            return val
    return -1
l =[1,2,90,86,645,98]
print(Linear_search(l,2))
