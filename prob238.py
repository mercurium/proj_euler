import time, string
START         = time.time()

SIZE          = 80846691 # Sum of the digits before the sequence starts repeating
ACTUAL_SIZE   = 2 * 10**15
s0            = 14025256
MOD           = 20300713

bbsRNG        = [s0]
bbsRollingSum = 0


while bbsRollingSum < SIZE + 1000:
  bbsRollingSum += sum(int(x) for x in str(bbsRNG[-1]))
  bbsRNG.append(bbsRNG[-1]**2 % MOD)

bbsString   = string.join([str(bbsNum) for bbsNum in bbsRNG], '')
bbsString   = [int(x) for x in bbsString]

bbsValue    = [1000] * (SIZE + 1)
bbsValue[0] = 0

for startIndex in xrange(100):
  if 1000 not in bbsValue:
    break
  print startIndex
  rollingSum = 0
  for endIndex in xrange(startIndex, len(bbsString)):
    rollingSum += bbsString[endIndex]
    if rollingSum > SIZE:
      break
    if startIndex + 1 < bbsValue[rollingSum]:
      bbsValue[rollingSum] = startIndex + 1

partSum  = sum(bbsValue)
leftover = ACTUAL_SIZE % SIZE
answer   = partSum * (ACTUAL_SIZE / SIZE) + sum(bbsValue[:leftover + 1])

print "Answer:", answer

print "Time Taken:", time.time() - START


"""
BLUM BLUM SHUB YO!

Going to do the dumb implementation first. Should be pretty straightforward from there.

There are 2,534,198 unique numbers that the BLUM BLUM SHUB rng will go through.
The digits sum up to 80,846,691. This means we'll repeat each number 5,637,620 times (+1 for some).

This means that...
  1 and 80,846,691 + 1
  2 and 80,846,691 + 2
  ...
  etc
will have the same p(n) value.

The max BBS value seems to be 89

Answer: 9922545104535661
Time Taken: 81.4870219231

Time Taken: 28.4292628765 # Turns out it's a lot faster if you don't do int -> str casts each time LOL


Congratulations, the answer you gave to problem 238 is correct.

You are the 690th person to have solved this problem.

Nice work, mercurium, you've just advanced to Level 12 .
525 members (0.08%) have made it this far.


"""
