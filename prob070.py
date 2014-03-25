import string, time
START = time.time()

totient = range(0,10**7) #compute all the totients
for i in xrange(2, len(totient)):
    if totient[i] == i:
        for j in xrange(i,len(totient),i):
            totient[j] *= (i-1.0)/i

minVal = 500 
minIndex = 0
for i in xrange(2,len(totient)): #find the number with the lowest ratio
    totient[i] = int(totient[i])
    if i%2 !=0 and i%3 != 0 and i%5 != 0 and \
      sorted( str(totient[i]) ) ==sorted( str(i) ) and \
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
