import time
START = time.time()

# 0 = prime, otherwise not prime.
primeCandidates = [True]*(2*10**6)

sumz = 2
count = 1
for i in xrange(3,len(primeCandidates),2):
    if primeCandidates[i]:
        sumz+=i
        for j in xrange(i**2,len(primeCandidates),2*i):
            primeCandidates[j] = False
        count +=1
            
print count
print sumz

print "Time Taken:", time.time()-START
