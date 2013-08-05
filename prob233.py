import time
start = time.time()

def gcd(a,b):
        if a == 0:
                return b
        return gcd(b%a,a)

SIZE = 10**5
SIZE_SQ = SIZE**2

iter_count = 0 
actual_count = 0 

vals = dict()

for m in xrange(1,SIZE):
	if 2*m**2 > SIZE:
		break
        for n in xrange(1,m+1):
		for k in xrange(1,SIZE):
			iter_count+=1
			N = 2*k**2*(m**2+n**2)
			if N > 2*SIZE:
				break
			a,b = 2*k**2*(m**2-n**2),4*m*n*k**2
			a,b = min(a,b),max(a,b)

			if N in vals:
				vals[N].add((a,b))
			else:
				vals[N] = set([(a,b)])
                	actual_count +=1 


print "I iterated over:", iter_count
print "But we only counted for:", actual_count

print "Count for 10000 is:", vals[10000]

sumz = 0
for key in vals.keys():
	if vals[key] == 140:
		sumz += key
		print key

print "Sum of the ones satisfying conditions is:", sumz
print "Time Taken:", time.time() - start

"""
I suspect that there are 386 items for 10**3, but for some reason, my new algorithm is only picking up 179... :/...


GRAAAH IT DOESN'T WORK TT___TT...
"""
