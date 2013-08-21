from math import log
import time
START = time.time()


vals = [0] + [log(i,10) for i in xrange(1,101)]

factorial_sums = [vals[0]] + [0] * (len(vals)-1)
for i in xrange(1, len(vals)):
	factorial_sums[i] = factorial_sums[i-1] + vals[i]


count = 0
for i in xrange(23,101): #starting at 23 since we're given that the first one is at 23.
	for j in xrange(0,i): 
		if factorial_sums[i] - factorial_sums[j] - factorial_sums[i-j]> 6:
			count = count + i - 2*j + 1
			break

print count
print "Time Taken: ",time.time()-START 

"""
13:28 ~/Desktop/python_projects/proj_euler $ python prob53.py 
4075
Time Taken:  0.00157308578491 (was original runtime)
Time Taken:  0.000264883041382 (new runtime after some refactoring)

"""
