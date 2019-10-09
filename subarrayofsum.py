
def subarraysum(l,s):
    d={}
    curr_s=0

    for i in range(len(l)):
        curr_s+=l[i]
        if curr_s==s:
            print('sum found between index 1 to',i+1)
        if curr_s-s in d:
            print('sum found between indexes', d[curr_s-s]+2, 'to',i+1)
            return
        d[curr_s]=i
        

    print('No subarray with given sum exists')

c=[1,2,3,7,5]
t=12

subarraysum(c,t)

c=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t=15
subarraysum(c,t)


