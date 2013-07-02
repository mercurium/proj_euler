from bitarray import bitarray

def primes_less_than(n):
	tmp = bitarray('0' * (n+1))
	prime_lst = [2]
	for i in xrange(3,n+1,2):
		if tmp[i] == 0:
			prime_lst.append(i)
			for j in xrange(i**2,n+1,2*i):
				tmp[j] = 1
	return prime_lst

