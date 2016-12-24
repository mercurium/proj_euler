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
    answersList   = numberArray[:]
    numberSumList = numberArray[:]
    newAnswersList = [0] * len(numberArray)
    newNumSumList  = [0] * len(numberArray)

    #Computing the next row of the problem
    for lengthOfChain in xrange(2, probSize+1):
        for start in xrange(0, probSize - lengthOfChain+1):
            end = start + lengthOfChain - 1

            val1 = numberArray[start] + numberSumList[start+1] - answersList[start+1]
            val2 = numberArray[end]   + numberSumList[start]   - answersList[start]

            newAnswersList[start] = max( val1, val2)
            newNumSumList[start]  = numberSumList[start] + numberArray[end]

        answersList, newAnswersList  = newAnswersList, answersList
        numberSumList, newNumSumList = newNumSumList, numberSumList

    return answersList[0]

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
Time Taken: 116.254349947 (I used lists instead of dictionaries and stopped making new ones. Holy shit that speed improvement
Time Taken: 96.1503489017 (removed expensive print statements)

This could almost definitely be cut in half if I just returned both values for noRepeatCost and repeatOnceCost in one call to dpSolver, but the runtime isn't that bad right now, and i'd prefer to leave it readable atm.

"""
