#NOTE TODO need to solve it
import time
START  = time.time()
SIZE   = 16
NUMDIG = 10

dataFile = open('data185.txt','r')
data     = dataFile.read()
data     = filter(len, data.split('\n'))

class Guess:
  def __init__(self, guessString):
    self.guess      = [int(x) for x in guessString.split()[0]]
    self.numCorrect = int(guessString.split()[1])

guesses = [Guess(guessString) for guessString in data]

nonOverlaps = set()
for gi1 in xrange(len(guesses)):
  for gi2 in xrange(len(guesses)):
    overlap    = sum([ (1 if guesses[gi1].guess[x] == guesses[gi2].guess[x] else 0) \
                      for x in xrange(len(guesses[gi1].guess)) ] )
    if overlap == 5:
      nonOverlaps.add((gi1,gi2))

print nonOverlaps, len(nonOverlaps), len(guesses)


overlapCounts = dict()
minOverlap    = SIZE
maxOverlap    = 0
for guess in guesses:
  for guess2 in guesses:
    if guess != guess2:
      numCorrect = guess.numCorrect + guess2.numCorrect
      overlap    = sum([ (1 if guess.guess[x] == guess2.guess[x] else 0) \
                        for x in xrange(len(guess.guess)) ] )
      try:
        overlapCounts[(numCorrect, overlap)] += 1
      except KeyError:
        overlapCounts[(numCorrect, overlap)] = 1


print "Time Taken:", time.time()-START

"""
9  21
2  21
6  12
1  19
20 19
0  10

"""




"""
  def recurse(pos, vals, appendedVals):
    if pos != 0:
      for g in sameSet[(pos-1,appendedVals[-1])]:
        vals[g] -=1
        if vals[g] < 0:
          return -1
    if pos == SIZE and vals == [0]*(len(guesses)):
      print pos, appendedVals, vals, "ANSWER"
      return appendedVals
    elif pos == SIZE:
      return -1
    for i in range(NUMDIG):
      if (pos,i) in sameSet:
        ans = recurse(pos+1, vals[:], appendedVals + [i])
        if ans != -1:
          return ans
    if pos < 6:
      print pos, appendedVals, vals
    return -1



  sameSet = dict()
  for g in range(len(guesses)):
    for index in range(SIZE):
      try:
        sameSet[(index,guesses[g][index])].add(g)
      except KeyError:
        sameSet[(index,guesses[g][index])] = set([g])
  for i in range(SIZE):
    for j in range(NUMDIG):
      if (i,j) in sameSet:
        print i,j, sameSet[(i,j)]

  entries = sameSet.keys()
  for entry in entries:
    if len(sameSet[entry]) < 2:
      del sameSet[entry]


"""
