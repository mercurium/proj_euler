#NOTE TODO need to solve it TURNITIN
import time, sys
START = time.time()
sys.setrecursionlimit(100)


SIZE = 10**6
pfactor = [0] * (SIZE+1)
for i in xrange(2,SIZE+1):
    if pfactor[i] == 0:
        pfactor[i] = i
        for j in xrange(i**2,SIZE,i):
            pfactor[j] = i

def factors(n):
    facts = []
    while n > 1:
        facts += [pfactor[n]]
        n /= pfactor[n]
    return sorted(facts)

def divisors(n):
    factorList = factors(n)
    divs = set([1])
    for factor in factorList:
        newSet = set()
        for elt in divs:
            newSet.add(factor * elt)
        divs = divs.union(newSet)
    divs.remove(n)
    divs.remove(1)
    return sorted(divs)

def sumDig(n):
    while n > 9:
        n = sum([int(x) for x in str(n)])
    return n

drsStored = dict()
def drs(n):
    if n in drsStored: #don't redo work
        return drsStored[n]
    if n < 10:
        return n
    maxVal = sumDig(n)
    for div in divisors(n):
        newVal = drs(n/div) + drs(div)
        if maxVal < newVal:
            maxVal = newVal
    drsStored[n] = maxVal
    return maxVal

def main():
    sumz = 0
    for i in xrange(2,SIZE):
        sumz += drs(i)
        if i %1024 == 0:
            print i
    return sumz

print main() 
print "Time Taken:", time.time() - START
"""
For this problem, find all possible factorizations, then compute the maxiumum digital root sum for each number. Like for example, if 24 pops up, we just return 11 since we know that 3x8 is the largest it can be. Therefore we recursively check all the possible factorizations and memoize results and reuse them.

Answer: 14489159
Time Taken: 20.2730100155

Congratulations, the answer you gave to problem 159 is correct.

You are the 1800th person to have solved this problem.
"""
