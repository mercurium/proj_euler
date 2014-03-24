import time
START = time.time()


#using this rather than a list so that I don't need to convert between str and int a lot later.
fifths = dict(  [ ( str(x), x**5) for x in xrange(0,10)] )

def fifth_sum(n):
	return sum([fifths[num] for num in str(n) ] )
	

sumz = 0
for i in xrange(3,9**6):  # We can cut off here since no numbers with more than 6 digits can be a sum of 5th powers. Reason, 10^6 > 9^5 * 7.
	if fifth_sum(i) ==i:
		sumz = sumz + i
		print i, sumz

print sumz
print "Time Taken:", time.time() - START
