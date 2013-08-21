import string
import time
START = time.time()

def reverse(num):
	return int(str(num)[::-1])

for a in range(999, 900, -1):
	for b in range(999,a,-1):
		c = a * b
		if reverse(c) == c:
			print c, a, b
			break


print "Time Taken:", time.time()-START
"""
Question: Find the largest palindrome that can be expressed as a product of two 3-digit numbers

This again was not a very hard problem.
Even with a naive way of checking all 1000^2/2 possibilities, that's only 500,000 multiplications to be done. In python, since checking for palindrome-ness can be done with val == int(str(val)[::-1]) pretty easily, we perform at most 500,000 operations.

Of course, we can optimize, like I did by not checking all of them because honestly, you're not going to get a max result when 'a' = 342.
"""
