import time
start = time.time()

SIZE = 15*10**4
lst = [0] * SIZE 
count = 0
for i in xrange(3,SIZE,2):
	if lst[i] == 0:
		for n in xrange(i**2,SIZE,i*2):
			lst[n]=1
		count+=1
	if count == 10001:
		print i
		break
		
print "Time Taken:", time.time()-start

"""
This question asks us to find the 10,001th prime

[tw-mbp13-jerrychen proj_euler (master)]$ python prob7.py
104743
Time Taken: 0.0393249988556

This problem is pretty simple as well. If you take the fact that there are approximately n/ln(n) primes <= n, then we know that since we want the 10,001st prime, we approximately want 10,001 = n/ln(n). As my code suggests, I overestimated the size by a bit but shortened the runtime by breaking as soon as I got to that number. The only problem with creating an arbitrarily high size for the limit is the space issue. However, since python seems to be fine with space until we go beyond 10^7 in array size, 1.5*10^5 isn't much worse than 1*10^5.

"""
