import time
START = time.time()
from primes import ncr
def cat(n):
	return ncr(2*n,n)/(n+1)
SIZE = 12

count = 0
for i in xrange(1,SIZE//2+1):
	a = ncr(SIZE,i)* ncr(SIZE-i,i)/2
	b = ncr(2*i,i)/2
	c = b - cat(i)
	d = a * c / b
	count +=d 
print "Answer is:", count 
print "Time taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 106 is correct.
You are the 2840th person to have solved this problem.

10:36 ~/Desktop/python_projects/proj_euler $ python prob106.py 
Answer is: 21384
Time taken: 0.0530858039856


So the interesting thing for this problem is, we only need to care about pairs that have an equal number of items. In other words, we only need to care about comparisons between subsets of the same size. This means that first off, we can throw away all comparisons between sets of different sizes (like size 1 vs size 3).

Next, if we think about it, we don't need to compare two sets {a,b} and {c,d} if a < b < c < d. We already know that a < c and b < d, which means their sum is going to be different.

The interesting thing is, you can see this as wanting sets that DO NOT satisfy the parenthesis matching problem (where you have n sets of '(' and ')' and you want to count how many possible combinations of ( and ) can be made so that they're matched correctly.

For n = 2, there's two cases ()() and (()). For n = 3, there's ((())), (()()), ()()(), (())(), ()(()), which comes out to 5 cases. Coincidentally, these are the catalan numbers, and we can see this as given numbers a,b,c,d,...etc, if there's a bigger number in set2 masking every number in set1, then we don't need to compare them.

Digressing along, the catalan numbers represent the types of subsets that we don't need to compare, but we need to check everything else. As a result, taking those two into account, we get an answer of 21384.

"""
