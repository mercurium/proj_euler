import time, string
from itertools import permutations as perm
START = time.time()

count = [0,0,0,0]
for i in perm('123456'):
    numbers = [int(x) for x in i]
    items = set()
    temp_count = 0
    for n in numbers:
        items.add((n,n))
        toRemove = set()
        for a in items:
            for b in items:
                if a[1] +1 == b[0]:
                    items.add((a[0],b[1]))
                    toRemove.add(a)
                    items.remove(b)
                    break
        for i in toRemove:
            
        temp_count = max(len(items),temp_count)
    count[temp_count] +=1
print count

print "Time Taken:", time.time() - START
