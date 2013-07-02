import time
start = time.time()
from bitarray import bitarray

size = 10**5/2
temp = bitarray('10' * size)
prime_lst = []
for i in xrange(3,len(temp),2):
	if temp[i] == 0:
		for j in xrange(i**2, len(temp),2*i):
			temp[j] = 1
		prime_lst.append(i)
prime_lst = prime_lst[2:]

test_lst = []
for i in xrange(17):
	for j in xrange(11):
		test_lst.append(2**i*5**j)
test_lst.sort()

sumz = 10
for i in prime_lst:
	for j in test_lst:
		if j > i:
			sumz += i
			break
		if pow(10,j,i) == 1:
			break
print sumz

print "Time Taken:", time.time() - start

"""
Main idea, we want to find a power such that 10^i = 1 mod p.
If i is a factor of 10^9, then that means that the repeat cycle 10^i mod p can be portioned into sizes of 10^9. In a weird way, that means that the numbers sum up to 0 mod p, which means 1111...111 mod p == 0 mod p.

Ex: 1+2+4 = 0 mod 7. Idk why... I forgot T.T;;;

Anyways, so I just need to check 1,2,4,5,8,...etc for the powers of the numbers to see if they'll have 1111...111 (10^9 1's) = 0 mod p. Fun exercise for you if you come back and forget what we did :)

Reusing the algorithm from 132, if something is a factor of a repunit, then we know that 10^i = 1 mod p, and i|10^n. This means that we once again only need to check 1,2,4,5,8,10,16,20,...etc, up to that number.

Made a stupid mistake here... forgot that xrange(num) is <num, not <= num =.=;;

~/Desktop/python_projects/proj_euler $python prob133.py
453647705
Time Taken: 0.36664390564
"""
