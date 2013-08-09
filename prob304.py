import time
start = time.time()
from primes import m_r 


#this takes a set of values and bases so that we can find x s.t.
#x = a1 mod b1
#x = a2 mod b2
#... and so on for any number of bases

def crt(bases, vals):  
  big_base = 1 
  sumz = 0 
  for val in bases: big_base *= val 
  for i in range(0,len(bases)):
    curr_base = big_base / bases[i]
    inverse = ext_gcd(bases[i],curr_base)[1]
    sumz += vals[i] * curr_base * inverse
  return sumz % big_base


def extended_gcd(a, b): #returns c,d such that ac+bd =1
  if b == 0:
    return (1, 0)
  else:
    q, r = a/b, a%b 
    s, t = extended_gcd(b, r)
    return (t, s - q * t)
ext_gcd = extended_gcd


#############################################################
##################### Getting 100,000 primes ################
#############################################################

i = 10**14
count = 0
prime_lst = []
while count < 10**5:
	i +=1
	if m_r(i):
		count +=1
		prime_lst.append(i)

print "Time Taken:", time.time() - start

#############################################################
##################  Finding the nth fibo num ################
#############################################################

pToTest = [3,7,13,67,107,630803]
fibo_lsts = []

for prime in pToTest:
	fib = [0,1,1,2]
	while fib[-1] != 1 or fib[-2] != 0:
		fib.append( (fib[-1] + fib[-2]) % prime)
	fibo_lsts.append(fib[:-2])

print "Time Taken:", time.time() - start

sumz = 0
for prime in prime_lst:
	vals = [ fibo_lsts[i][prime% len(fibo_lsts[i]) ] for i in xrange(len(pToTest)) ]
	ans = crt(pToTest,vals)
	sumz += ans

print sumz % mod
print "Time Taken:", time.time() - start


"""
61548431626872586 is the answer I'm getting... it's apparently wrong? =/...
LOL oops, forgot to take the sum mod 1234567891011... ehehehe... :x. But yeah, rest were solved :)
283988410192

Congratulations, the answer you gave to problem 304 is correct.

You are the 978th person to have solved this problem.
"""
