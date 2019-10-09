def getmissingno(a):
    n=len(a)
    total=(n+1)*(n+2)/2
    
    sumof_a=sum(a)
    print(total,sumof_a)
    return int(total-sumof_a)

a=[1, 2, 3, 4, 5, 6, 7, 8,9,11]

print(getmissingno(a))
