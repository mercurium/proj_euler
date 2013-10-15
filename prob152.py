import time
START = time.time()
from primes import factor, is_prime

MAX_SIZE =37
num_iter = 0

inverse = [0,0] + [1./x**2 for x in range(2,MAX_SIZE+1)]
partial_sums = [inverse[-1]]
for i in xrange(MAX_SIZE):
	partial_sums.append(partial_sums[-1] + inverse[MAX_SIZE-i-1])
partial_sums = partial_sums[::-1]

print [round(x,3) for x in partial_sums]

nums = [1,1,1] + [( 1 if (factor(n)[-1] > 7) else 0) for n in xrange(3,MAX_SIZE)]

def recurse(n,num,denom):
	global num_iter
	if num_iter % (2**18) == 0:
		print num_iter, n
	num_iter +=1
	if num*2 > denom or n > MAX_SIZE or num*1./denom + partial_sums[n] < .4999999:
		return 0
	if num * 2 == denom:
		print int(denom**.5), factor(int(denom**.5)), n-1
		return 1
	while n < MAX_SIZE and n*3 > MAX_SIZE and nums[n] == 1:
		n+=1
	if n > MAX_SIZE:
		return 0
	a,b = recurse(n+1,num,denom), recurse(n+1,num*n**2+denom, denom* n**2)
	return a+b


numer = 4*9 + 4*16 + 9*16
denom = 4*9*16

print recurse(5,numer,denom), num_iter
print "Time Taken:", time.time() - START
