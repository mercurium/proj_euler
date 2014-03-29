#NOTE TODO need to solve it
import time, math
START = time.time()

width, height = 3,7
MOD = 135707531

import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    if r < 0: return 0
    prod = 1
    for i in xrange(n, n-r,-1):
        prod *= i
    prod /= math.factorial(r)
    return prod % MOD


def gcd(a,b):
    while a != 0:
        a,b = b%a,a
    return b

count = 0

count += ncr((width+1) * (height+1), 4) #All sets of four points.
count %= MOD
print count

#Now get rid of all sets of 4 points where they're all on the same line or 3 on the line. diagonals
for h in xrange(1,height/2+1):  #h and w are the slopes of the line
    for w in xrange(1,width/2+1):
        length = min(width/w, height/h)
        if gcd(w,h) != 1:
            continue
        a,b = width - w *length, height - h * length
        bottom = 0
        for c in xrange(length, 1,-1):
            index = length - c
            top = (a + w * index + 1 ) * (b + h * index +1)
            num = top - bottom  #we want the number of lines of length "length", and no the lines >"length"
            bottom = top

            # 2 since diagonals go both ways, ncr(length+1,3) for the 3 points on the line
            # ((width +1) * (height +1) - length -1) for the points off of that line
            count -= 2*num * ncr(length+1, 3) * ((width +1) * (height +1) - length - 1)
            if length >= 3:
                count -= 2*num * ncr(length +1,4)
            print h, w, a, b, c , top, bottom
    print h, count
            
count -= (height+1) * ncr(width+1,3) * (height * (width+1))  # rows (3 points in a line, 1 point elsewhere)
count -= (width+1) *  ncr(height+1,3) * (width * (height+1)) # columns
count -= ncr(width+1,4) * (height+1) + ncr(height+1,4)*(width+1) #4 points on the same line
print count % MOD
print "Time Taken:", time.time() - START

for i in xrange(0, (width+1)*(height+1)):
    for j in xrange(i):
        for k in xrange(j):
            w1,h1 = i%(height+1), i/(height+1)
            w2,h2 = j%(height+1), j/(height+1)
            w3,h3 = k%(height+1), k/(height+1)
            if (w2 - w1) * (h3-h1) == (w3 - w1) * (h2-h1): # This only happens if they're on the same line.
                continue
            area = (w1 * h2 + w2 * h3 + w3 * h1 - w1 * h3 - w2 * h1 - w3 * h2 )
            if area < 0: area *= -1 # supposed to go counter clockwise, if you go clockwise at first, it's negative.
            boundary = gcd(abs(w1-w2),abs(h1-h2)) + gcd(abs(w2-w3),abs(h2-h3)) + gcd(abs(w3-w1),abs(h3-h1)) 
            count +=  (area - boundary +2)


print count % MOD
print "Time Taken:", time.time() - START
