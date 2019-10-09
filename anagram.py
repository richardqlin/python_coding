l= ['acb','cba','bca','ef','fe','d','bac']


d = {}

for i in l:
    k = ''.join(sorted(i))
    if k in d:
        d[k].append(i)
    else:
        d[k]=[i]
s=[]
for k,v in d.items():
    s.append(tuple(v))
print(d)
print(s)
d = {}

for i in l:
    key = ''.join(sorted(i))
    if key in d:
        d[key].append(i)
    else:
        d[key] = []
        d[key].append(i)
print(d)

s = []

for k,v in d.items():
    s.append( tuple(v))

print(s)

