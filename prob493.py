import time
START = time.time()

BALLS_OF_EACH_COLOR = 10
NUM_COLORS          = 7
TOTAL_NUM_BALLS     = 70
TOTAL_BALLS_GRABBED = 20

memoizationDict = dict()
def getProbNewBall(numUnlocked, numLeft):
  # Base Case
  if numLeft == 0:
    return numUnlocked

  # Memoization case
  if (numUnlocked, numLeft) in memoizationDict:
    return memoizationDict[(numUnlocked, numLeft)]

  chanceUnlockNew = (TOTAL_NUM_BALLS - numUnlocked * BALLS_OF_EACH_COLOR) * 1.0 \
      / (BALLS_OF_EACH_COLOR - (TOTAL_BALLS_GRABBED - numLeft))

  memoizationDict[(numUnlocked,numLeft)] = \
    getProbNewBall(numUnlocked + 1, numLeft -1) * chanceUnlockNew + \
    getProbNewBall(numUnlocked, numLeft - 1) * (1. - chanceUnlockNew)
  return memoizationDict[(numUnlocked, numLeft)]

print getProbNewBall(0,20)
print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 493 is correct.

You are the 37th person to have solved this problem.

Answer: 6.81874180202
Time Taken: 0.0002601146698

This problem was pretty easy, the main idea is that we can compute the probability of adding in a new color at each step, and use dynamic programming on (numColorsUnlocked, numBallsLeft) to figure out the probability of a new color being picked, and we multiply the probabilities of each event happening at each step to get the total expected value.

Even cooler is the fact that this solution is not the optimal one. I'm leaving this solution here since it was pretty fast anyways, but there's a closed math form of:
  7 * ( 1 - ncr(60,20)/ncr(70,20))

The basis for this form is that each color has a (ncr(60,20)/ncr(70,20)) chance of NOT being picked, which means it has a (1 - ncr(60,20)/ncr(70,20)) chance of being picked. By linearity of expectation and symmetry, that means that E[ # colors] = 7 * E[1 particular color being picked] =
  7 * ( 1 - ncr(60,20)/ncr(70,20))

  yup yup :3

"""
