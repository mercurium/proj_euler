import time
START = time.time()



def reverse(num):  # This feels slightly unnecessary, but w/e, it does make the code a bit clearer...
	return str(num)[::-1]
	
sumz = 0

for i in xrange(1,10): #numbers from 0-9
	if reverse(bin(i)[2:]) == bin(i)[2:]:
		print i, bin(i)
		sumz = sumz + i
for i in xrange(1,1000): #numbers with an even # of digits
	num = int(str(i) + reverse(i))
	if reverse(bin(num)[2:]) == bin(num)[2:]:
		print num, bin(num), i
		sumz = sumz + num

for i in xrange(1,100): # numbers with an odd # of digits.
	for j in xrange(0,10):
		num = int(reverse(i) +str(j)+ str(i))
		if reverse(bin(num)[2:]) == bin(num)[2:]:
			print num, bin(num)
			sumz = sumz + num
print sumz
print "Time Taken:", time.time() - START
