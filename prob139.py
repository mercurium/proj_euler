import time
START = time.time()

SIZE = 10**8
pythagTriplet = set()
count = 0

for m in xrange(1,SIZE):
    if 2*m*(m+1) > SIZE:
        break
    diff = 2 if m%2 == 0 else 1
    nLim = SIZE/(2*m) - m
    
    for n in xrange(1,min(m,nLim+1),diff):
        d,f = m*m,n*n
        a,b,c = d-f,2*m*n,d+f
        if a+b+c >= SIZE:
            break
        if a > b:
            a,b = b,a
            
        if c %(b-a) == 0:
            for k in xrange(1,SIZE/(2*(d+f))+1):
                pythagTriplet.add((a*k,b*k,c*k))

print len(pythagTriplet)
print "Time Taken:", time.time()-START


"""
~/Desktop/python_projects/proj_euler $python prob139.py
10057761
Time Taken: 253.662650108 (slow, naive method)
Time Taken: 26.9965119362 (reordered the loops)

Method of attack: a = m^2-n^2,b = 2mn, c = m^2 +n^2
So we know that since we can tile the square, we have (b-a)|c.
After this, we only need to check the k's when we have a valid equation... :x

"""
