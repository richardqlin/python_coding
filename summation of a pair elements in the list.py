l=[1,2,3,4,5,6,7]

s=int(input('what is sum of a pair?'))

b={}
b[l[0]]=0

for i in l[1:]:
    diff=s-i
    if diff in b:
        print(i, diff)
    else:
        b[i]=0
