import time
START = time.time()

primes = []
primeCheckLst = range(500)
for i in range(2,len(primeCheckLst)):
    if primeCheckLst[i] == i:
        for j in range(i**2,len(primeCheckLst),i):
            primeCheckLst[j] = 0
        primes.append(i)
partitionVal = dict()
    
def compute(n):
    def countPartitions(n, pos):
        if (n,pos) in partitionVal: #memoization
            return partitionVal[(n,pos)]
        if n==0 or pos == len(primes):
            return 1
        if primes[pos] > n:
            return 0
        partitionVal[(n,pos)] = countPartitions(n,pos+1) + countPartitions(n-primes[pos], pos)
        return partitionVal[(n,pos)]

    partitionVal[n] = countPartitions(n,0)
    return partitionVal[n]

for i in xrange(1,1000):
    if compute(i) > 5000:
        print i
        break
  
print "Time Taken:", time.time() - START
