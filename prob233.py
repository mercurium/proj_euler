#NOTE need to solve TODO
import time
start = time.time()

def gcd(a,b):
        if a == 0:
                return b
        return gcd(b%a,a)

SIZE = 10**5

iter_count = 0 
actual_count = 0 

vals = dict()

for m in xrange(1,SIZE):
	if m**2 > SIZE:
		break
        for n in xrange(1,m+1):	
		item = m**2+n**2
		if item > SIZE:
			break
		for k in xrange(1,SIZE):
			iter_count+=1
			N = k*(item)
			if N > SIZE:
				break
			a,b = k*(m**2-n**2),2*m*n*k
			a,b = min(a,b),max(a,b)

			if N in vals:
				vals[N].add((a,b))
			else:
				vals[N] = set([(a,b)])


print "I iterated over:", iter_count, "numbers"

print "Count for 10000 is:", len(vals[10000])*8-4

sumz = 0
for key in vals.keys():
	if len(vals[key]) == 53:
		sumz += key
		print key

print "Sum of the ones satisfying conditions is:", sumz
print "Time Taken:", time.time() - start

"""
I suspect that there are 386 items for 10**3, but for some reason, my new algorithm is only picking up 179... :/...


GRAAAH IT DOESN'T WORK TT___TT...
"""
