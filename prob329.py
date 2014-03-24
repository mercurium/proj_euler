import time
start = time.time()
from bitarray import bitarray
import string

SIZE = 500
ROUND = 15
SEQ = '000011000100101'

def gcd(a,b):
        if a == 0:
                return b
        return gcd(b%a,a)

primes = bitarray('11'+'0' *(SIZE-1))
for i in xrange(2,SIZE+1):
        if primes[i] == 0:
                for j in xrange(2*i,(SIZE+1),i):
                        primes[j] = 1

seq = bitarray(SEQ)
squares = [0] + [1] * SIZE 
new = squares[:]
div = 3**ROUND * SIZE * 2**(ROUND)

#print squares[1:] #########################

#croak then jump... =/...
for i in xrange(0,ROUND):

        for j in xrange(1,SIZE+1):
                if seq[i] == primes[j]:
                        new[j] *= 2
    #print new[1:], "prime multiply, aka croak" ####################

        squares = new[:]
        new = [0]*(SIZE+1)

        new[1] = squares[2]
    new[2] = squares[1]
    new[SIZE-1] += squares[SIZE]
        new[SIZE] = squares[SIZE-1]
        for j in xrange(2,SIZE):
                new[j] += squares[j-1] + squares[j+1]
    #print new[1:], "redistributing, aka jump"  ########################

squares = new[:]
a = sum(squares)
shared = gcd(a,div)
a,div = a/shared, div/shared
print str(a) + '/' + str(div)

print "Time Taken:", time.time() - start


"""
Congratulations, the answer you gave to problem 329 is correct.

You are the 954th person to have solved this problem.

15:07 ~/Desktop/python_projects/proj_euler $ python prob329.py 
199740353/29386561536000
Time Taken: 0.00684404373169

OKAY! So i pretty much had this one solved when I left it but I didn't follow up on it...
So the main problem that I had was that I was doing a jump and then a croak, and not realizing that they croaked on the original spot too... SIGHHHH TT___TT... ANYWAYS...

So each turn has two steps, a croak then a jump. Keeping the numbers discrete, we can compute this as such, if it's a prime and the croak is a prime number, multiply it by 2, otherwise by 1. Same for other cases etc.

Then for jumping, rather than making it fractional, just add the probability of spot j to spots j-1 and j+1 for turn T+1...

Afterwards, compare the total number to what the divisions would have been. Since each croak has a 1/3 or 2/3 chance of happening, we want to divide the total by 3^#ROUNDS and since each jump can go either way, we want to divide it by 2^#ROUNDS, and by the total number of squares, aka #SIZE
"""
