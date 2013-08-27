import time
START = time.time()
from bitarray import bitarray

p_lst = bitarray('10'*50000)
p_lst[2] = 0
for i in xrange(3,len(p_lst),2):
	if p_lst[i] == 0:
		for j in xrange(i*i,len(p_lst),2*i):
			p_lst[j] = 1




print "Time Taken:", time.time() - START
