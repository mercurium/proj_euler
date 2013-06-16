import time
start = time.time()
from math import log
#from bitarray import bitarray

size = 10**7
#tmp = bitarray('010' +'01' *(size//4+1))
tmp = [0,1,0] + [0,1] * (size//4-1)
prime_lst = [2]
for i in xrange(3,len(tmp),2):
	if tmp[i] == 0:
		for j in xrange(i**2,len(tmp),2*i):
			tmp[j] = 1

		prime_lst.append(i)


print "Time Taken:", time.time() - start
print len(prime_lst)
sumz = 0


for val in xrange(len(prime_lst)):
	i = prime_lst[val]
	if i**2 > size: #we're done at this stage
		break
	switch = False
	for j in prime_lst[val+1:]:
		val1 = i*j
		if val1 > size: #if we've exceeded, we're done?
			break
		if switch:
			sumz += val1
			continue
		

		if i*val1 > size:
			sumz += val1
			switch = True
			continue

		maxz = i * j
		val3 = 1
		while maxz * i <= size:
			maxz *= i
			val3 +=1
		
		if j*j*i > size:
			sumz += maxz
		else:
			val2 = i
			while val2*j <= size:
				num = val2 * j
				while num * j <= size:
					num*= j
				if num <= size and num > maxz:
					maxz = num
				val2 *= i
			sumz+=maxz




print sumz

print "Time Taken:", time.time() - start

"""
10^4's answer:


16368310
Time Taken: 0.00457787513733

10^5:
1414000891
Time Taken: 0.0762510299683
"""
