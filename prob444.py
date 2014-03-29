#NOTE TODO need to solve it
import time, math
START = time.time()


N = 10**7
K = 20

import operator as op
def ncr(n, r):
	r = min(r, n-r)
	if r == 0: return 1
	num = reduce(op.mul, xrange(n, n-r, -1))
	denom = reduce(op.mul, xrange(1, r+1))
	return num//denom

sumz = 0
k = ncr(N + K,K)
for i in xrange(1, N+1):
	k =  k *(N-(i-1))/(N+K-(i-1))
	sumz += k * 1.0 / i
print sumz

print "Time Taken:", time.time() - START



"""
Notes!

-At each step, if you do not take someone else's ticket, you can only do worse from what you're at. 
-Suppose that you could improve by getting ticket 'k'. The other person would only switch tickets with you if you have the highest ticket shown at the moment. Therefore, it is not beneficial for you to take anyone else's ticket. 

And the problem is, if you scratch your ticket, it WILL be taken away if it is better than your previous one (if you're last person with an unscratched ticket, person giving you it knows that it isn't better than what you currently have),

or is worse than what you have in hand.


Therefore, 

HERP.... E(n) = E(n-1) + 1/n... >.>;;;
Reason for this is, E(n) = (sum(E(1...n-1))/n +1), since the only people who don't take the tickets are those that are see the rest of them are the lowest k tickets left. This results in a recursive problem, if the ticket worth $1 is on the 10th person, then it's been reduced to a problem of size (n-10) and then +1 to account for the 1 being placed down.

Anyways, now we want a continuous summation of this thing... T>T...

D(n) = 1/n
E(n) = sum(1/(1...n))
S_1(n) = sum(E(1...n))

"""
