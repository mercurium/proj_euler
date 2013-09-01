import time
import math
START = time.time()



def fiver(n):
	if n == 0: return 0
	return sum([ n/5**x for x in xrange(1,9)])

def twoer(n):
	if n == 0: return 0
	return sum([ n/2**x for x in xrange(1,19 ) ])

SIZE = 2*10**5 # =200000
fivepow = fiver(SIZE) -12
twopow = twoer(SIZE) -12

twos = [0,0] + [twoer(i) for i in xrange(2,SIZE+1)]
fives = [0,0] + [fiver(i) for i in xrange(2,SIZE+1)]

print "Time taken:", time.time() - START

count = 0
for x in xrange(0,0,SIZE+1):
	for y in xrange(x, SIZE):
		if x+y > SIZE:
			break
		z = SIZE - x - y
		if z <y: break
		if fives[x] + fives[y] + fives[z] <= fivepow and twos[x] + twos[y] + twos[z] <= twopow:
			count += 1
	print x
count *= 6
for x in xrange((SIZE+1)/2):
	z = SIZE - 2*x
	if x*2 + z > SIZE: break
	if fives[x] *2 +fives[z] <= fivepow and twos[x]*2 + twos[z]  <= twopow:
		count +=3

print count
print "Time taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 154 is correct.

You are the 1282nd person to have solved this problem.

wrote it in java since it was taking so long in python...

The answer is:479742450
Time taken: 7.158960073

"""
