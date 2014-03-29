#NOTE TODO need to solve it
import time
from math import log
START = time.time()
SIZE = 20

counts = [0]*int(log(SIZE,3)+1)
for i in range(50):
    if 3**i < SIZE:
        counts[i] = int(log(SIZE/(3**i),2)+1)



vals = dict()
vals[ (0,) * len(counts)] = 1

queue = [(0,)* len(counts)]
while len(queue) != 0:
    nextVals = queue.pop(0)
    a = list(nextVals)
    for i in range(len(a)):
        if (i == 0 or a[i] < a[i-1]) and a[i] < counts[i]:
            a[i]+=1
            a = tuple(a)
            if a in vals:
                vals[a] += vals[nextVals]
            else:
                vals[a] = vals[nextVals]
            if a not in queue:
                queue.append(a)
            a = list(a)
            a[i] -=1

print len(vals)
print vals[tuple(counts)]

print "Time Taken:", time.time() - START
