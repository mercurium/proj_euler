import time
from primes import lcm
START = time.time()

SIZE  = 31
count = -2 # Need to exclude n = 1 from the count.

numOccur = 1

for i in xrange(1,SIZE + 1):
    numOccurNext = lcm(numOccur, i+1)
    count += ((4**i) / numOccur - 4**i / numOccurNext)

    numOccur = numOccurNext

print count


print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 601 is correct.

You are the 313th person to have solved this problem.

Answer: 1617243
Time Taken: 0.000152111053467 

Yay! The length of a streak of a number n is the number of numbers k for which n = 1 mod k.

So 60 = lcm(1,2,3,4,5,6) gives us that 61 has streak of 6. So we just look up all the lcms of the products and then subtract off the ones that have the next element in the lcm.


"""
