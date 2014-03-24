import time
START = time.time()

# 0 = prime, otherwise not prime.
prime_candidates = [0]*(2*10**6)

sumz = 0
count = 0
for i in xrange(3,len(prime_candidates),2):
	if prime_candidates[i] == 0:
		sumz+=i
		for j in xrange(i**2,len(prime_candidates),2*i):
			prime_candidates[j]+= 1
		count +=1
			
print count
print sumz

print "Time Taken:", time.time()-START
