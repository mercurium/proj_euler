from itertools import *
import string
import time
from primes import ncr

#The overall sum is: 209110240768
#Time Taken: 39.4977288246
#http://en.wikipedia.org/wiki/De_bruijn_sequence would help me learn how to solve this more efficiently... T__T

start = time.time()
num_dig = 5
prefix = '1' +('0'*num_dig) +'1'
size = 2**num_dig - len(prefix)

def test(n): #basically this part checks if each number is in the set....
	if len(n) != size: 
		return 0
	
	m = prefix + n + prefix
	for i in product('10',repeat=num_dig):
		i = string.join(i,'')
		if i not in m: return 0
	return int('1'+n+'1',2)

def main(): #makes a list of all possibilities and iterates through them
	sumz = 0
	count = 0
	for i in combinations(range(size),2**(num_dig-1) -2):
		num = 0
		for j in i: num+= 10**j
		num = '0' * (size-len(str(num))) + str(num)
		val = test(num)
		if val> 0:
			sumz+= val
			count +=1
	print "The overall sum is:", sumz
	print "numbers needed:", count

main()
print "Time Taken:", time.time() -start

#the method of attack for this problem was: so we know that there has to be a sequence of 1000001 somewhere in the problem, so we don't need to bother making strings that don't even have this value. But what we did instead was iterate through all strings that have this property then manually check if each set of [01]*5 was in there xD. Not the best method ever, and the 40 second runtime reflects this.
