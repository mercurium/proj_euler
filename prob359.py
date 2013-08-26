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

large_num = 71328803586048 #Given input number, not something I made up.
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


(off by one error may occur in explanation for the sake of conciseness, look at code to get exact answer)
Okay, so first off, I was curious and iterated out all the floors that people would be on. While doing that, I noticed that the number of times each square formed a pair of two adjacent rooms appears on is (n^2 - (n-1)^2)/2 ( +1 if n is odd)

After thinking about it for a bit, it makes sense. After all, any number that was small enough to be used for n^2 wouldn't make its way up to n^2. In addition, I noticed that the difference between each of the neighbors on a floor were consecutive squares, makes sense in hindsight but I didn't notice till I saw the layout of the numbers...

Then, I realized that the first person on each floor was approximately n^2/2 . This is because they were the last ones to not get paired up, which means they couldn't find a partner for (n-1)^2. Then, this means that the r'th person on the f'th floor was f^2/2 if r = 1, otherwise P(f,r) = <some_square> - P(f,r)
The only thing left to do at this point was to figure out what that <some_square> was. It wasn't actually too bad to do because hey, the first difference between P(f,1) and P(f,2) is n^2, meaning P(f,r) = (f+r-2)^2 - P(f,r-1) 

This isn't too bad to calculate for small r... unfortunately, we wre dealing with... 7 * 10^13.... we wouldn't be able to compute recurrence relations in any reasonable amount of time. Thankfully... we have this...
P(f,r) = (f+r-2)^2 - P(f,r-1) = (f+r-2)^2 - ( (f+(r-1)-2)^2 - P(f,(r-1)-1)) = (f+r-2)^2 - (f+r-3)^2 + P(f,r-2) = ... etc.

Anyways, the point was that we had discovered an alternating sum of squares (plus the first element). This meant that we could express it in one expression and save us a LOT of computational time. And yeah, that's my answer/code/solution/lolmath xDD.

"""
