def maxSubarraysum(a):
    max_so_far=-1
    max_end=0

    for i in range(len(a)):
        max_end=max_end+a[i]
        if max_so_far<max_end:
            max_so_far=max_end

        if max_end<0:
            max_end=0
    return max_so_far


a=[1, 2, 3, -2 ,5]
print(maxSubarraysum(a))
