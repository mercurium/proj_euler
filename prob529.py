import time
from primes import ncr
START     = time.time()
SEED_SIZE = 12
SIZE      = 30
MOD       = 10**9 + 7

# (current array, num Dig must satisfy, array sum)
newDigDict = dict()
for i in range(1,10):
  newDigDict[((i,), 1, i)] = 1

# This part is grosser, but also a constant runtime since I have a faster portion below. Hence, I'm going to update the bottom part first.
solutions = [0,0]
for numDig in xrange(2,SEED_SIZE):
  currentSum     = 0
  digDict        = newDigDict
  newDigDict     = dict()
  newLocToOldLoc = dict()
  START          = time.time()
  for key in digDict.keys():
    currArr, numDigSatisfy, arraySum = key
    for newDig in xrange(1,10):
      newArray         = list(currArr)[:] + [newDig]
      newNumDigSatisfy = numDigSatisfy + 1
      newArraySum      = arraySum + newDig
      while newArraySum > 10:
        if newNumDigSatisfy >= len(newArray):
          break
        newArraySum -= newArray.pop(0)

      # Can skip out early and avoid polluting our dictionary with junk entries
      if newArraySum > 10:
        break

      if newArraySum == 10:
        newNumDigSatisfy  = 0
        newArraySum      -= newArray.pop(0)
        currentSum       += digDict[key]
      if (tuple(newArray), newNumDigSatisfy, newArraySum) in newDigDict:
        newDigDict[(tuple(newArray), newNumDigSatisfy, newArraySum)] += digDict[key]
      else:
        newDigDict[(tuple(newArray), newNumDigSatisfy, newArraySum)]  = digDict[key]

      # setup memoization to be faster later
      if (tuple(newArray), newNumDigSatisfy, newArraySum) in newLocToOldLoc:
        newLocToOldLoc[(tuple(newArray), newNumDigSatisfy, newArraySum)] += [key]
      else:
        newLocToOldLoc[(tuple(newArray), newNumDigSatisfy, newArraySum)] = [ key ]

  solutions.append(currentSum)
  currentSum = 0
  for digit in xrange(2,len(solutions)):
    currentSum += ncr(numDig, digit) * solutions[digit] % MOD
    #print numDig, "digit:", digit, "multiplier:", ncr(numDig, digit), "\tnumSol for", digit, ':', solutions[digit], "\ttotal count:",  ncr(numDig, digit) * solutions[digit]
  print numDig, currentSum % MOD, '  \t', len(newDigDict), '\t', "Time Taken:", time.time() - START

# bigger chunk of the problem. Making some small tracking changes can give us a speedup of up to 14x ...which is still not enough for 10^18 LOL
for numDig in xrange(SEED_SIZE, SIZE):
  digDict    = newDigDict
  newDigDict = dict()
  START      = time.time()
  answerSums = 0

  # slowest part of the code atm is this for loop...
  for newLoc in newLocToOldLoc.keys():
    newDigDict[newLoc] = sum([digDict[oldLoc] for oldLoc in newLocToOldLoc[newLoc]])

  for key in newDigDict.keys():
    if key[1] == 0:
      answerSums += newDigDict[key]

  solutions.append(answerSums)
  for digit in xrange(2,len(solutions)):
    currentSum += ncr(numDig, digit) * solutions[digit] % MOD
  print numDig, currentSum % MOD, '  \t', len(newDigDict), '\t', "Time Taken:", time.time() - START

print sum([len(x) for x in newLocToOldLoc.keys()])

print "Time Taken:", time.time() - START

"""

  Okay. If we want to find the number of solutions of length 'n', we know that we can...
  1) Append a 0 to the end of a solution of length 'n-1'
  2) Combine two non-solutions that end with some sums 'k' and '10-k'. Ex: a string of length 4 can be made by combining '12' and '34'
  3) Append a solution of length 'm' to a solution of length 'n-m'. Ex: a string of length 4 can be made by combining '37' and '46'

  Huh. Intersting thought. A string summing up to 10 with no 0s in it is of at most length 10 (ten 1's in a row...). Since we can stick 0's anywhere (but the front) without affecting anything, we actually want #solutions for 10^SIZE + (10^SIZE-1) * #solutions for (10^SIZE-1) excluding 0s + ... + (10^SIZE - 1 choose k) * (# solutions for k excluding 0s)

  thought while writing that down. We might be able to DP keep track of all the possible sets of numbers that add up to at most 9. It *shouldn't* actually be that many states... There's going to be 2^9 = 512 cases where the numbers add up to 9. But if we don't care about the order... which means it's up to 1023 cases that we need to iterate on.

  But... if we care about potential answers that might use some numbers that were already used earlier... Okay. We can definitely slim this down a bit.

  Worst case scenario that we'll need to check is 1023 * 9.

  Actually... We also need to keep track of how many elements of the ones listed that we still need to satisfy.

  I'm seeing... 1024 possible ends, 9 possible next digits (lolol zeroes), and 9 possible number of digits we need to satisfy....

  ...gg. Worst case each digit we update, we need to do 100k checks each... ...for a 10^18 number... >.>;
  Okay. I did the empirical thing and tested it out. Looks like it's capped at 2806 * 9 iterations. So it's 25,254 calculations. Still bad, but only 1/4th as bad as I put it as originally. I also think we can probably shave it off a bit.

Alright. I've dropped ^ down to 8418 computations per update. This still requires me to know the previous results though... so I can't actually make it faster than O(n) atm... and seriously, it's going to be closer to O(n^2)...



"""
