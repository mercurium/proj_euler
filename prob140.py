import time
start = time.time()

values = [1,2,5]
count = 0
mult = 1.9
mult_old = 3.1

for i in xrange(1,30):
	val = values[-1]
	num = int((val-1) * mult)
	while True:
		a = 5*num**2 - num * 16 + 4
		if a > 0 and int(a**.5)**2 == a:
			values.append(num)
			print num, values[-1]/(1.0*values[-2])
			mult,mult_old = mult_old, (values[-1]-2.)/(1.0*values[-2])
			break
		num+=1
		count +=1

print count
print sum(values[:32]) -93
print "Time Taken:", time.time() - start
"""
I just need to find the 30th solution where 5n^2-16n+4 is a square...


OKAY. So I found my mistake. First off, the equation we had to find was (2x-3)/(x^2+x-1) = a. HOWEVER, since we're not counting the 0th term, the a that we find is actually -3. Thus the one we want to find is actually (2x-3)/(x^2+x-1) = a+3...

So I need to subtract 3 from all of my results... :/... whoops.
"""
