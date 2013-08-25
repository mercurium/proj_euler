import time
start = time.time()
from math import *
fa = factorial
from primes import factor

size = 20

def log10(n):
	return log(n)/log(10)

total = sum([log(n) for n in range(2,size+1)])
total = int(1000*total+.5)/1000.

vals = [int(1000*log(n)+.5)/1000. for n in factor(fa(size))[:-1]]


print total
print vals, sum(vals)

goal_val = total/3.
prev_seen = {}

def helper(n,pos):
	if (n,pos) in prev_seen:
		return prev_seen[(n,pos)]
	#base case
	if pos >= len(vals) or n >= goal_val:
		return n
		
	a = abs(goal_val - helper(n+vals[pos],pos+1))
	b = abs(goal_val - helper(n,pos+1))
	c = abs(goal_val - n)
	if a < b and a < c:
		prev_seen[(n,pos)] = helper(n+vals[pos],pos+1)
	if c < a and c < b:
		prev_seen[(n,pos)] = [(n,pos)]
	else:
		prev_seen[(n,pos)] = helper(n,pos+1)
		return prev_seen[(n,pos)]

#we will proceed to attempt this problem using knapsack.





