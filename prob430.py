import time
START    = time.time()

NUM_ITER = 4000
SIZE     = 10**10
MAN_COMP = 15 * 10**6

def computeSpot(m, N, numIter): 
    chanceNoFlip = ((m-1.)**2 + (N - m)**2) / N**2
    n = 1.0
    for i in xrange(numIter):
        n = n * chanceNoFlip + (1-n) * (1-chanceNoFlip)
    return n

total = 0
for i in xrange(1,MAN_COMP+1):
    n = computeSpot(i, SIZE, NUM_ITER)
    total += n
    if i % 2**16 == 0:
        print i, n

print total * 2 + (SIZE - MAN_COMP*2) / 2
print "Time taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 430 is correct.

You are the 581st person to have solved this problem.

Time taken: 280.965759039 (desktop pypy)

The chance for a single spot m to flip is the chance that both random numbers are picked on the same side of it. Aka, both in front or both behind it. So the chance is ( (m-1)^2 + (N - m)^2) / N^2. Let's call this "chanceNoFlip"

Then Pr(White at kth flip) = Pr(White at kth-1 flip) * chanceNoFlip + Pr(Black at kth-1 flip) * chanceFlip.

After some number of flips, the answer normalizes to being 50% (it does this for all spots given sufficiently many flips, but the ones on the edges take much longer). For the middle 10^10 - (15*10^6), 4000 is sufficient to exclude them as a margin of error and say that their chance of being white is 50%. For the rest of the tiles, it's pretty straighforward to compute their chance by using the formula above. Score.


"""
