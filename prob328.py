#NOTE TODO need to solve it
import time
START = time.time()
import sys
sys.setrecursionlimit(120)

SIZE = 100
mc = dict() #mc for min cost
minVal = dict()


def compute_min(l, u): #l,u for lower and upper limits
    if (l,u) in mc:
        return mc[(l,u)]
    if u <= l: #1 or less numbers to compare
        return 0
    if u == l+1: #two numbers to compare
        return l
    if u == l+2: #three numbers to compare, check the middle one
        mc[(l,u)] = l+1
        return l+1
    minz = 10**10
    for i in range(u, l/2+u/2, -1):
        value = i + max(compute_min(l,i-1), compute_min(i+1,u))
        if value < minz:
            minz = value
        else:
            break
    mc[(l,u)] = minz

    #mc[(l,u)] = min([ i+ max(compute_min(l,i-1), compute_min(i+1,u)) for i in range(l/2+u/2,u) ])
    return mc[(l,u)]

ans = 0
for i in xrange(1,SIZE+1):
    ans += compute_min(1,i)
print ans

print compute_min(1,SIZE)
print "Time taken:", time.time()-START

#for i in range(1,100):
#    print i + max(compute_min(1,i-1), compute_min(i+1, 100)),


"""
Okay, this result memoizes the previous answers to see which one is the best, but it's slow so idk...
gotta do better than this...

Hm... so I tried doing binary search to find the optimal division, but since the optimal choice might not be the only local minimum.

"""
