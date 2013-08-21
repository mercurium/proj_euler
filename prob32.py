import time
import string
START = time.time()


solution_set = set()

# I split the cases to save up on runtime
for i in xrange(1,10):  #the two multipliers can either be 1 dig x 3 dig or 1 dig x 4 dig
	for j in xrange(123,9876):
		n = str(i) + str(j) + str(i*j)
		if string.join(sorted(str(n)),'') == '123456789':
			solution_set.add(i*j)
			print i, j, i*j

for i in xrange(1,99): # or 2 dig x 3 dig.
	for j in xrange(123,988):
		n = str(i) + str(j) + str(i*j)
		if string.join(sorted(str(n)),'') == '123456789':
			solution_set.add(i*j)
			print i, j, i*j
print sum(solution_set)
print "Time Taken:", time.time() - START
