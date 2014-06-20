import time
from math import log
START = time.time()
SIZE = 10**6
END_CASE = int(math.log(SIZE,3))

def prime_gen(size): #Find all primes < the input size
    primes = [2]
    ints = [0,1,2] + [1,2] *(size/2-1)
    for i in xrange(3,size,2):
        if ints[i] == 1:
            for j in xrange(i**2,size,i*2):
                ints[j] = i
            ints[i] = i
            primes.append(i)
    return primes


prevComputedValues = dict()
def recurse(threePow, twoPow, runningSum): # Int, Int, Int
    if threePow == END_CASE:
        if runningSum in prevComputedValues:
            prevComputedValues[runningSum] += 1
        else:
            prevComputedValues[runningSum] = 1
        return

    for i in range(0, twoPow):
        nextPartitionItem = 2**i * 3**threePow
        if nextPartitionItem + runningSum > SIZE:
            break
        recurse( threePow +1, i, runningSum + nextPartitionItem)
    recurse(threePow +1, twoPow, runningSum)



primes = prime_gen(SIZE)
recurse(0, int(math.log(SIZE, 2) + 1), 0)

sumz = 0
for p in primes:
    if p in prevComputedValues and prevComputedValues[p] == 1:
        sumz += p

print sumz
print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 333 is correct.

You are the 610th person to have solved this problem.

3053105
Time Taken: 69.4968202114

For this problem, valid solutions have partitions of the form 2^i * 3^j, and all numbers in the partition have the trait that i1 > i2 iff j1 < j2. Then, this means that we just need to find all possible decreasing subsequences and we get our answer.

"""
