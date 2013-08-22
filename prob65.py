import string
import time
START = time.time()
lst = [1]*100
lst[0] = 2

for i in xrange(0,len(lst)):
	if i %3 == 2:
		lst[i] = (i//3+1)*2


a = 1
b = lst[-1]
for i in xrange(len(lst)-2,0,-1):
	b_n = lst[i]*b+a
	a = b
	b = b_n

a = a + lst[0]*b

print a, b

a = str(a)
sumz = 0
for i in xrange(0,len(a)):
	sumz += int(a[i])
	
print sumz

print "Time Taken:", time.time()-START
