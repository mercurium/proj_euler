import time


START = time.time()
numRounds = 15

roundsWins = dict()

roundsWins[(1,1)] = .5
roundsWins[(1,0)] = .5
for i in range(2,100):
    roundsWins[(i,0)] = 1/(i+1.)

for rounds in range(2,numRounds+1): # keep track of how many rounds there have been
    i = rounds
    for wins in range(1,rounds+1):
        j = wins
        roundsWins[(i,j)] = roundsWins[(i-1,j-1)] * 1./(i+1)
        if i > j:
            roundsWins[(i,j)] += roundsWins[(i-1,j)] * i/(i+1.0)

sumz = 0
for j in range(rounds//2+1,numRounds+1):
    sumz += roundsWins[(numRounds,j)]

print "Answer for", numRounds, "is:", int(1./(sumz)-.01), sumz
print "Time Taken:", time.time() - START
