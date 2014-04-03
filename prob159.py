#NOTE TODO need to solve it TURNITIN
import time
START = time.time()

size = 10**6
pfactor = [0] + [1,2]*(size//2)
for i in xrange(3,size,2):
    if pfactor[i] == 1:
        pfactor[i] = i
        for j in xrange(i**2,size,i*2):
            pfactor[j] = i

def factors(n):
    if n <= 1:
        return []
    facts = []
    while n > 1:
        facts += [pfactor[n]]
        n /= pfactor[n]
    return sorted(facts)

def divisors(n):
    factorList = factors(n)
    if len(factorList) == 0:
        print "ERROR"
        return "ABBAIOIRJER"
    divs = set([factorList[0]])
    for factor in factorList:
        newSet = set()
        for elt in divs:
            newSet.add(factor * elt)
        divs = divs.union(newSet)
    return sorted(divs)

drsStored = dict()
def drs(n):
    if n in drsStored: #don't redo work
        return drsStored[n]
    if n < 10:
        return n
    maxVal = drs(sum([int(x) for x in str(n)]))
    for div in divisors(n):
        newVal = drs(n/div) + drs(sum([int(x) for x in str(div)]))
        if maxVal < newVal:
            maxVal = newVal
    drsStored[n] = maxVal
    return maxVal

def main():
    sumz = 0
    for i in xrange(2,size):
        sumz += drs(i)
        if i %1024 == 0:
            print i
    return sumz
print main() 
print "Time Taken:", time.time() - START
"""
Answer: 54216812
Time Taken: 52.1227741241

"""
