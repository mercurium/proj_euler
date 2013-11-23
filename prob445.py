import time
from primes import m_r
START = time.time()

count = 0
SIZE = 10**5
mod = 10**9 +7


def get_pfactor(SIZE):
	pfactor = range(0,SIZE+1)
	for i in xrange(2,len(pfactor)):
		if pfactor[i] == i:
			for j in xrange(i*2,len(pfactor),i):
				pfactor[j] = i
	return pfactor


pfactor = get_pfactor(SIZE)
print "Part 1 done!"

val_dict = {2:5,5:5}
for n in range(1,SIZE/2+1):
	k = SIZE - n
	while k != 1:
		p = pfactor[k]
		if p in val_dict:
			val_dict[p] +=1
		else:
			val_dict[p] = 1
		k /= p
	r = n;
	while r != 1:
		p = pfactor[r]
		val_dict[p] -=1
		r /= p
	prod = 1
	for factor in val_dict.keys():
		if val_dict[factor] == 0:
			continue
		prod = ((1 + pow(factor, val_dict[factor],mod)) * prod) % mod
	count += prod*2
	if n% 100 == 0:
		print n
count -= prod
print (count - pow(2,SIZE,mod)+2) % mod
print "Time Taken:", time.time() - START
