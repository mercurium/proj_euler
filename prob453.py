import time, math
START = time.time()

width, height = 12345,6789

import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    if r < 0: return 0
    num = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return num//denom


def gcd(a,b):
    if a% 2 == 0 and b % 2 == 0:
        return 2 #not correct, but we just need to see if the two are rel. prime.
    while a != 0:
        a,b = b%a,a
    return b

count = 0

count += ncr((width+1) * (height+1), 4) #All sets of four points.
print count

#Now get rid of all sets of 4 points where they're all on the same line or 3 on the line.
for h in xrange(1,width+1):
    if height/h < 2:
        break
    for w in xrange(1,height+1):
        if width/w < 2:
            break
        length = min(width/w, height/h)
        if gcd(w,h) != 1:
            continue
        a,b = width - w *length, height - h * length
        bottom = 0
        for c in xrange(length, 1,-1):
            index = length - c
            top = (a + w * index + 1 ) * (b + h * index +1)
            num = top - bottom
            bottom = top

            count -= 2*num * ncr(length+1, 3) * ((width +1) * (height +1) - length - 1)
            if length >= 3:
                count -= 2*num * ncr(length +1,4)
    print h
            
print count
count -= (height +1 ) * (width * (height+1) * ncr(height+1, 3) - ncr(height+1,4))
print count
count -= (width+1) * (height * (width+1) * ncr(width+1, 3) - ncr(width+1,4))

print count
print "Time Taken:", time.time() - START
