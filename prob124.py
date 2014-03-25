import time
START = time.time()
numRad = [1]*100001

for i in xrange(1,len(numRad)):
    if numRad[i] == 1:
        for j in xrange(i,len(numRad),i):
            numRad[j] *= i
    numRad[i] = (numRad[i],i)

numRad = numRad[1:] #toss out 0th element
numRad.sort()
print numRad[9999][1]  #get answer 

print "Time Taken:", time.time() - START
