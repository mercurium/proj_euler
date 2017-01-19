import time, random
START = time.time()

numGames = 10**8
winCount = 0

for game in xrange(numGames):
  lastNum1   = 0
  lastNum2   = 0
  runningSum = 0
  while runningSum < 1:
    lastNum1 = random.random()
    runningSum += lastNum1
  while runningSum < 2:
    lastNum2 = random.random()
    runningSum += lastNum2
  if lastNum2 > lastNum1:
    winCount += 1


print winCount * 1.0 / numGames

print "Time Taken:", time.time() - START
