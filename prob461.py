#NOTE TODO need to solve it
import time, random
from math import e, pi,log
START = time.time()
SIZE = 200

minErr = 10**-6
val = [e**(i*1.0/SIZE)-1 for i in range(20000)]
count = 0
points = []


for a in range(1,SIZE):
    sa = val[a]
    for b in range(a, SIZE):
        sb = sa + val[b]
        if sb > pi:
            break
        for c in range(b,SIZE):
            sc = sb + val[c]
            if sc-.0001 > pi:
                break
            d = int(log(pi+1-sc) * SIZE)
            sd = sc + val[d]
            if abs(pi -sd) < minErr:
                points.append([a,b,c,d])
                count +=1
            d = int(log(pi+1-sc) * SIZE)+1
            sd = sc + val[d]
            if abs(pi -sd) < minErr:
                points.append([a,b,c,d])
                count +=1

print "Found", count, "possible locations"
print "Time Taken:", time.time() - START
