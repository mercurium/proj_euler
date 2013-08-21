import time
START = time.time()

def is_rotation(a,b):
	return sorted(str(a)) == sorted(str(b))


for i in xrange(10**5,3 * 10**5):
	if is_rotation(i,2*i) and is_rotation(i,3*i) and is_rotation(i,4*i) and is_rotation(i,5*i) and is_rotation(i,6*i):
		print i, 2*i, 3*i,4*i,5*i,6*i
		break


print "Time Taken:", time.time()-START

"""
In hindsight, the fact that we're dealing with x,2x,3x,4x,5x,6x means that it should be a repeater of cycle length 6. Which means that 10^6 = 1 mod p for some p, Obviously, this means that p should be 7. Shame I didn't see it while I was solving the problem...
"""
