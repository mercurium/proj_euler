import time
START = time.time()

#returns 1^2+ 2^2 + ... + n^2
def sumOfSq(n):
    return n * (n+1) * (2*n+1) / 6

sumOfSqs = [sumOfSq(n) for n in xrange(0,10**4+1)]
palindSq = set() #set to avoid duplicates

for sumEnd in xrange(2,len(sumOfSqs)):
    for sumStart in xrange(sumEnd-2, -1, -1):
        n = sumOfSqs[sumEnd]-sumOfSqs[sumStart]
        if n > 10**8:
            break
        if str(n) == str(n)[::-1]: 
            palindSq.add(n)

palindSq =list(palindSq)
print sum(palindSq),len(palindSq)

print "Time Taken:", time.time() - START


#2906969179, there's two duplicates.
#run time of 1.116 seconds :D
