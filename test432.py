import time
start = time.time()

size = 10**6
mod = 10**9
debug = False

def setup():
	lst = [0] + [1,2] * (size//2+1)
	for i in xrange(3,size+1,2):
		if lst[i] == 1:
			lst[i] = i
			for j in xrange(i**2,size+1,2*i):
				lst[j] = i
	return lst	

def pfactor(n):
	if n > size:
		return "Too big fool"
	if n == 1:
		return []
	list_of_factors = []
	while n > 1:
		list_of_factors.append(factor_lst[n])
		n /= factor_lst[n]
	return list_of_factors 

def main():
	sumz =0
	for i in xrange(1,size+1):
		temp_set = set([2,3,5,7,11,13,17])
		num_factors = pfactor(i)
		temp_prod = 1
		for j in num_factors:
			if j in temp_set:
				temp_prod *= j
			else:
				temp_prod *= j-1
				temp_set.add(j)
		sumz += temp_prod%mod
	return (sumz*92160)%mod

def test():
	assert(sorted(pfactor(50)) == [2,5,5])
	assert(sorted(pfactor(6)) == [2,3])
	assert(pfactor(0) == [])
	assert(pfactor(1) == [])
	return True

factor_lst = setup()
print "Time Taken:", time.time() - start
print main()
if debug: test()
print "Time Taken:", time.time() - start
