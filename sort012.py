def sort012(a):
    z=0
    t=len(a)-1
    o=0
    while o<=t:
        if a[o]==0:
            a[z],a[o]=a[o],a[z]
            z+=1
            o+=1
        elif a[o]==1:
            o+=1
        else:
            a[o],a[t]=a[t],a[o]
            t-=1
        #print(a)
    return a

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

print(sort012(arr))
