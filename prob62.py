import time
import string
START = time.time()

cubic_nums_sorted = {}
for i in xrange(0,10000):
	m = string.join(sorted(str(i**3) ),'' )
	cubic_nums_sorted[m] = (cubic_nums_sorted[m] + [i]) if m in cubic_nums_sorted else [i]
	if len(cubic_nums_sorted[m]) == 5:
		print min(cubic_nums_sorted[m])**3, min(cubic_nums_sorted[m])
		break
print "Time Taken:", time.time()-START
