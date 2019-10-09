def equilibrium(a):
    left=0
    right=0
    n=len(a)

    for i in range(int(n/2)):
        left+=a[i]
        right+=a[n-i-1]
        if left==right:
            return i+1
    return -1

arr = [-7, 1, 5, 2, -4, 3, 0] 
print (equilibrium(arr)) 
        
        
