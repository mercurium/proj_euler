import time
START = time.time()

N = 24
lim = 2**(2*N-2)
n = 2**(N-1)

def splittable(val):
	if val[2] == 1:
		return True
	x,y, leng = val
	a = (x - n)**2 + (y - n)**2.  # top left corner 
	b = ((x+leng-1) - n)**2 + ((y+leng-1) - n)**2 #bottom right corner
	c = (x - n)**2 + ((y+leng-1) - n)**2 # bottom left corner 
	d = ((x+leng-1) - n)**2 + (y - n)**2 # top right corner

	a,b,c,d = a>lim, b> lim, c > lim, d>lim
	return a == b == c == d


count = 1
lst = [(0,0,2**(N-1)), \
		(2**(N-1),0, 2**(N-1)), \
		(0, 2**(N-1),2**(N-1)), \
		(2**(N-1),2**(N-1),2**(N-1)) ]
while len(lst) > 0:
	val = lst.pop()
	if splittable(val):
		count += 2
		#if val[2] != 1: print val
	else:
		count += 1
		lst.append((val[0],val[1],val[2]/2))
		lst.append((val[0]+val[2]/2,val[1],val[2]/2))
		lst.append((val[0],val[1]+val[2]/2,val[2]/2))
		lst.append((val[0]+val[2]/2,val[1]+val[2]/2,val[2]/2))
	#print len(lst), sum([x[2]**2 for x in lst])

print count

#for x in xrange(2**N):
#	for y in xrange(2**N):
#		if (x - 2**(N-1))**2 + (y - 2**(N-1))**2 <= 2**(2*N-2):
#			print 0,
#		else:
#			print 1,
#		if y == 2**(N-1)-1:
#			print '|',
#	print
#	if x == 2**(N-1)-1:
#		print '-'*(2**(N+1)+1)
print "Time Taken:", time.time() - START


"""
The key to this problem is realizing that as soon as you split up the main box, you only have to check to see if the four corners are the same in order to get your answer.

Congratulations, the answer you gave to problem 287 is correct.

You are the 805th person to have solved this problem.


313135496
Time Taken: 368.990906 

"""
