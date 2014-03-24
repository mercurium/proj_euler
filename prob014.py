import time
START = time.time()

collatz_values = dict()
collatz_values[1] = 0
maxz = 0
max_key = 0

def collatz(i):
	if collatz_values.get(i,-1) == -1:
		if i % 2 == 0:
			temp = 1 + collatz(i/2)
		else:
			temp = 1 + collatz(3 * i + 1)
		collatz_values[i] = temp
	return collatz_values[i]

for i in xrange(2,10**6):
	if collatz(i) > maxz:
		maxz = collatz(i)
		max_key = i
		
		
print maxz, max_key

print "Time Taken:", time.time() - START
