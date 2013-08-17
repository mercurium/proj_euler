import string
import math
import time
start = time.time()

pentas = set()
for i in xrange(1,50000):
	pentas.add(i*(3*i-1)/2)

penta_lst = [ i * (3*i-1)/2 for i in xrange(10000)]

done = 0
for i in xrange(2,10000):
	for j in xrange(1,i):
		a = penta_lst[i] 
		b = penta_lst[j] 
		if a+b in pentas and a-b in pentas:
			print a-b, a, b, a+b
			print i,j
			done = 1
			break
	if done:
		break


print "The answer is:", a-b
print "Time Taken:", time.time()-start
