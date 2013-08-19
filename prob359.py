import time
START = time.time()
from primes import factor



"""
dummyP is a dumber implementation of finding P(f,r), which was my checker to make sure my program was functioning correctly.
"""
def dummyP(f,r): 
	if f == 1:
		return r*(r+1)/2
	if r <= 1:
		return int(f**2/2)
	if r == 2:
		return (f+((f+1)%2))**2 - dummyP(f,r-1)
	return (f+((f+1)%2) + r-2)**2 - dummyP(f,r-1)

def sq_sum(n):
	return n*(n+1)*(2*n+1)/6

def sum_sq(start,end):
	return sq_sum(end) - sq_sum(start)

def P(f,r):
	if f == 1: # not sure why we need to special case f = 1, but it's a bit glitchy 
		return r*(r+1)/2
	if r <= 1: # First number that begins each floor is the one that couldn't be place anywhere else.
		return int(f**2/2)
	start = f + (f+1)%2 -1
	end =   f + r - 1 - (f%2)
	if r % 2 == 0: #There's a similar formula for when it's odd, but it's cleaner when even, so I just recursed to an even one from odd starting points.
		initial_sum = sum_sq(start,end)
		part_removed = sum_sq(start/2,end/2) * 8
		return initial_sum -  part_removed - P(f,1)
	return (f+((f+1)%2)+r-2)**2 - P(f,r-1)   # was lazy only wanted to compute on case.
	
""" These are the test cases to make sure I was getting the expected result:"""
print "P(1,1) is:", P(1,1) == 1
print "P(1,2) is:", P(1,2) == 3
print "P(2,1) is:", P(2,1) == 2
print "P(10,20) is:", P(10,20) == 440
print "P(25,75) is:", P(25,75) == 4863
print "P(99,100) is:", P(99,100) == 19454

large_num = 71328803586048
factors = factor(large_num)

print "factorized 71328803586048",  factors

vals = {2:0,3:0,1:0}
for i in factors:
	vals[i] +=1
print vals

sumz = 0
for i in xrange(vals[2]+1):
	for j in xrange(vals[3]+1):
		n = 2**i*3**j
		m = large_num/n
		sumz += P(n,m)

print "Final answer is:", sumz  % 10**8
print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 359 is correct.

You are the 628th person to have solved this problem.

~/Desktop/python_projects/proj_euler $python prob359.py 
P(1,1) is: True
P(1,2) is: True
P(2,1) is: True
P(10,20) is: True
P(25,75) is: True
P(99,100) is: True
factorized 71328803586048 [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3L, 1]
{1: 1, 2: 27, 3: 12}
Final answer is: 40632119
Time Taken: 0.096107006073


will type up solution later, fingers hurt from using this keyboard... :[...
"""
