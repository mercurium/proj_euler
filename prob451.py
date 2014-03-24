import time
START = time.time()
SIZE = 10**4

def pfactor_gen(size): #for each number n, return some factor of it.
    stuff = range(size)
    for i in xrange(2,size):
        if stuff[i] == i:
            for j in xrange(i*2,size,i):
                stuff[j] = i
    return stuff

pfactor = pfactor_gen(SIZE+1)

def calc(n):
    if pfactor[n] == n:
        return 1
    for j in xrange(n-pfactor[n], n//2-1, -pfactor[n]):
        if j + 2 != n and ((j+1)**2-1) % i == 0:
            return j+1
        if ((j-1)**2-1) % i == 0:
            return j-1
    return 1


START = time.time()
sumz = 0
for i in xrange(3, SIZE+1):
    if i% 1024 == 0:
        print i
    val = calc(i)
    sumz += val
    #print i, val
print sumz

print "Time Taken:", time.time() - START

"""
Solve the problem of... x^2 = 1 mod n...
(x+1)(x-1) = 0 mod n... dammit. I should have something in my book about this T.T.... LOL... look back at code from prob407. It's the same darn problem...


Congratulations, the answer you gave to problem 451 is correct.

You are the 24th person to have solved this problem.

Return to Problems page.

153651073760956
Time Taken: 183.206949205 seconds (in Java)



"""
