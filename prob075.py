import time
START = time.time()

SIZE = 1500
rightTriangle = dict()

for m in xrange(2,SIZE):
    if m**2 > 1500000: break
    for n in xrange(1,m):
        val = 2*m*(m+n)

        if val > 1500000: break
        for k in xrange(1,125001):
            valz = k * val
            if valz > 1500000: break
            a,b = m*m*k - n*n*k, 2*m*n*k
            if a > b:
                a,b = b,a
            if valz not in rightTriangle:
                rightTriangle[valz] = set()
            rightTriangle[valz].add((a,b))
         
count = sum([ (len(rightTriangle[perim]) == 1) for perim in rightTriangle.keys()])

print count
print "Time Taken:", time.time()-START

#http://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
#161667
#Time Taken: 9.80598711967 (on laptop)
#Time Taken: 4.45831394196 (on desktop)

