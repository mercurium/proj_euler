import time
START = time.time()
MOD   = 10**9 + 7
SIZE  = 10**8

#   Input: Size of array
#   Output: (array of non-repeating elements, array of repeating elements)
def getNumberSequences(size):
    allNumHash  = set([0])
    numberArray = [0]
    num         = 0
    repeatIndex = SIZE+1

    for index in xrange(2,SIZE+1):
        num = (num **2 + 45) % MOD
        if num in allNumHash:
            repeatIndex = numberArray.index(num)
            break
        allNumHash.add(num)
        numberArray.append(num)

    nonRepeatingNumArr = numberArray[:repeatIndex]
    repeatingNumArr    = numberArray[repeatIndex:]
    return (nonRepeatingNumArr, repeatingNumArr)

def dpSolver(numberArray):
    probSize      = len(numberArray)
    answersDict   = dict()
    numberSumDict = dict()
    for i in xrange(probSize):
        answersDict[(i,i)]   = numberArray[i]
        numberSumDict[(i,i)] = numberArray[i]

    #Computing the next row of the problem
    for lengthOfChain in xrange(2, probSize+1):
        print lengthOfChain
        newAnswersDict = dict()
        newNumSumDict  = dict()
        for start in xrange(0, probSize - lengthOfChain+1):
            end = start + lengthOfChain - 1
            newAnswersDict[(start,end)] = max( \
                    (numberArray[start] \
                        + numberSumDict[(start+1, end)] \
                        - answersDict[(start+1, end)]), \
                    (numberArray[end] \
                        + numberSumDict[(start, end-1)] \
                        - answersDict[(start, end-1)])
            )
            newNumSumDict[(start,end)] = numberSumDict[(start,end-1)] + numberArray[end]

        answersDict   = newAnswersDict
        numberSumDict = newNumSumDict

    return answersDict[(0, probSize-1)]


nonRepeatingNums, repeatingNums = getNumberSequences(SIZE)

print len(nonRepeatingNums), len(repeatingNums)

if len(repeatingNums) == 0:
    answer = dpSolver(nonRepeatingNums)
else:
    repeatLen        = SIZE - len(nonRepeatingNums)
    wrapAround       = repeatLen % len(repeatingNums)
    numRepeat        = repeatLen // len(repeatingNums)
    nonRepeatingNums = nonRepeatingNums + repeatingNums[:wrapAround]
    repeatingNums    = repeatingNums[wrapAround:] + repeatingNums[:wrapAround]
    noRepeatCost     = dpSolver(nonRepeatingNums)
    repeatOnceCost   = dpSolver(nonRepeatingNums + repeatingNums)
    repeatCost       = repeatOnceCost - noRepeatCost
    answer           = noRepeatCost + repeatCost * numRepeat

print "The answer is:", answer
print "Time Taken:", time.time() - START

"""
Notes:

For size = 10^8, and mod = 10^9 + 7, 
The first number to repeat is 535424698,first occuring when index = 57956, and repeats at 65205
The cycle is 7248 ints
57956 + 7248 * 13788 + 6620
    = 64576 + 7248 * 13788

Congratulations, the answer you gave to problem 477 is correct.

You are the 168th person to have solved this problem.

The answer is: 25044905874565165
Time Taken: 7318.35272813

"""
