import string
import time
start = time.time()
temp = open('prob8input.txt','r')

l = temp.read()

maxz = 0
total = len(l)

for i in xrange(0, total - 5):
	val = int(l[i]) * int(l[i+1]) * int(l[i+2]) * int(l[i+3]) * int(l[i+4])
	if maxz < val:
		maxz = val
		
print maxz
print "Time Taken: " + str(time.time()-start)

"""
read the values as a string, int-ify each digit, one at a time, compute product, return largest one
"""
