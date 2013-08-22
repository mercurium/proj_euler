from primes import *
from math import sqrt
import math
import time
START = time.time()

"""
the way to get the next item in the list is such:
 A' = a*B -A
 B' = (d-A'*A')/B
 a' = int((sqrt(d)+A')/B')
"""
def get_next_iter(A,B,a,d):
	A = a*B-A
	B = (d-A*A)/B
	a = int((sqrt(d)+A)/B)
	return A,B,a

count = 0
for d in xrange(2,10000): #iterate from 2 to 10000
	if int(sqrt(d+.2))**2 != d:
		next_iter =get_next_iter(0,1,int(sqrt(d)),d)
		lst_A =[next_iter[0]]
		lst_B =[next_iter[1]]
		lst_a =[next_iter[2]] #this updates the list
		
		next_iter =get_next_iter(lst_A[0],lst_B[0],lst_a[0],d)
		lst_A += [next_iter[0]]
		lst_B += [next_iter[1]]
		lst_a += [next_iter[2]] #this updates the list again
		i=1
		while lst_A[-1]!=lst_A[0] or lst_B[-1]!=lst_B[0] or lst_a[-1] != lst_a[0]: #while it hasn't repeated yet...
			next_iter =get_next_iter(lst_A[i],lst_B[i],lst_a[i],d)
			lst_A += [next_iter[0]]
			lst_B += [next_iter[1]]
			lst_a += [next_iter[2]]
			i+=1 #our fancy loop counter


		if len(lst_a)%2 == 0: #if it has an odd cycle, add to count
			count += 1
print count
print "Time Taken:", time.time()-START
