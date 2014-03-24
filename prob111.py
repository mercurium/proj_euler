import time
START = time.time()
from primes import mr

mult = 1111111111
successes = set()
sumz = 0
for big_dig in xrange(9,0,-1):
    n = big_dig * mult
    for dig in xrange(0,10):
        for diff in xrange(big_dig-9,big_dig+1):
            m = n - diff*10**dig
            if mr(m) and m > 10**9:
                successes.add(big_dig)
                sumz += m
print "Digits we've seen:", successes
print "Time taken:", time.time() - START

for big_dig in xrange(9,0,-1):
    if big_dig in successes:
        continue
    n = big_dig * mult
    for dig,dig2 in ((a,b) for a in xrange(10) for b in xrange(a)):
        for diff,diff2 in ((d1,d2) for d1 in xrange(big_dig-9,big_dig+1) for d2 in xrange(big_dig-9,big_dig+1)):
            m = n - diff*10**dig - diff2*10**dig2
            if mr(m) and m > 10**9:
                successes.add(big_dig)
                sumz += m

print "Digits we've seen:", successes
print "Time taken:", time.time() - START

pow1, pow2 = 10**9, 0
for dig1 in xrange(1,10):
    n = dig1 * pow1 
    for dig2 in xrange(10): 
        m = n + dig2 * 10**pow2
        if mr(m):
            print m
            sumz += m

print sumz
print "Time taken:", time.time() - START
"""

Congratulations, the answer you gave to problem 111 is correct.
You are the 3407th person to have solved this problem.


~/Desktop/python_projects/proj_euler $python prob111.py 
Digits we've seen: set([1, 3, 4, 5, 6, 7, 9])
Time taken: 0.15297794342
Digits we've seen: set([1, 2, 3, 4, 5, 6, 7, 8, 9])
Time taken: 0.199028015137
612407567715
Time taken: 0.202805995941


Okay, so once again, my 'mr' (short for miller_rabin) function is a prime testing function, and as such, I'm using it to test the primality of these numbers. I noticed that all the numbers could have a "run" of length 8 or 9 in a 10 digit number so I stopped my function there. If there were cases where it would have taken more than just that, I could have done it recursively as well. Anyways...

Start off with assuming that the answer is the simplest it can be, aka that there's a 10 digit number with 9 of its digits being one identical digit. If that fails, test it for 8 of that digit. Since we're only testing 10 * 9/2 * 9 * 9 < 40000 numbers, we're not having a problem with constantly using the primality test...

Ugh, sorry for anyone reading this, this wasn't a good explanation =/... Basic idea was that you test if there's 9 of a digit for each digit, then test if there's 8 of a digit, then you're done (0 is a special case since it has to have a number at the leading and end digit.)
"""
