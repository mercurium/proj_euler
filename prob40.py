import string
import time
START = time.time()

A = range(10**6)
B = [str(x) for x in A]
C = string.join(B,"")
prod = 1
for i in xrange(7):
	prod *= int(C[10**i])
	print C[10**i]

print "answer is: ", prod
print "Time Taken:", time.time() - START
