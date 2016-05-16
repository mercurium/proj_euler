import string, time
START = time.time()

totient = range(0,10**7) #compute all the totients
for i in xrange(2, len(totient)):
    if totient[i] == i:
        for j in xrange(i,len(totient),i):
            totient[j] *= (i-1.0)/i

totient = [int(x) for x in totient]

print "Time Taken:", time.time() - START
minVal   = 500 # starting seed
minIndex = 0   # keep track of index with largest ratio

# find the number with the lowest ratio
# The number with the smallest ratio is not divisible by 2,3,or 5.
# because otherwise it would be too small. 2|n -> 2*phi(n) <= n
for i in xrange(3,len(totient), 2):
    totient[i] = int(totient[i])
    if i%3 != 0 and i%5 != 0 and \
      sorted( str(totient[i]) ) == sorted( str(i) ) and \
      i*1.0/totient[i] < minVal:
        minVal = i*1.0/totient[i]
        minIndex = i

print "The number with the lowest ratio was:", minIndex, "with a ratio of", minVal
print "Time Taken:", time.time() - START

"""
Main idea of the problem, compute all of the totients of each number. You can do this quickly using a modification of the sieve.

Then, check if totient values are permutations by using sorted(num) == sorted(totient(num))

Then compute the ratio and voila, you get the answer

"""
