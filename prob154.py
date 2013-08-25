import time
import math
START = time.time()



def fiver(n):
	if n == 0: return 1
	return sum([ n/5**x for x in xrange(1,int(math.log(n,5)+1) ) ])

def twoer(n):
	if n == 0: return 1
	return sum([ n/2**x for x in xrange(1,int(math.log(n,2)+1) ) ])

SIZE = 2*10**5 # =200000
fivepow = fiver(SIZE) -12
twopow = twoer(SIZE) -12

twos = [0,0] + [twoer(i) for i in xrange(2,SIZE+1)]
fives = [0,0] + [fiver(i) for i in xrange(2,SIZE+1)]

print "time elapsed = " + str(time.time()-START)

count = 0
eqcount = 0
for x in range(0,SIZE+1):
	for y in range(0,x+1):
		if x + y > SIZE: break
		z = SIZE - x - y
		if z >y: continue
		if fives[x] + fives[y] + fives[z] <= fivepow and twos[x] + twos[y] + twos[z] <= twopow:
			count += 1
			if x == y:
				eqcount +=1
	print x

print count, eqcount
print count * 2 + eqcount
print "Time taken:", time.time() - START
