import string
import time
START = time.time()

max_dig_sum= 0
max_a, max_b = 0,0
for a in range(50,100):
	for b in range(50,100):
		n = a**b
		dig_sum = sum([int(dig) for dig in str(n)])
		if max_dig_sum< dig_sum:
			max_dig_sum= dig_sum
			max_a,max_b = a,b

print max_dig_sum, max_a,max_b
print "Time Taken:", time.time() - START
