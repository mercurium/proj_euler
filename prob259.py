import time
from fractions import Fraction as Fr
START = time.time()
SIZE = 9

def concat(lst): #Turns something like [1,2,3,4,5] -> 12345
    sumz = lst[0]
    for i in range(1,len(lst)):
        sumz *= 10
        sumz += lst[i]
    return sumz

answers = dict() # (start, stop) : set(possible combos)
def countPossibilities(start, stop):
    if start == stop:
        return set([start])

    #memoize results, don't repeat work
    if (start, stop) in answers: 
        return answers[(start, stop)]

    currentAnswer = set()
    for index in range(start, stop):
        if stop - start >= 4: # This is just for me to see progress
            print stop-start, index, start, stop
        frontSet = countPossibilities(start,index)
        backSet  = countPossibilities(index+1,stop)
        for a in frontSet: #For each pair a,b try all four possible actions.
            for b in backSet:
                currentAnswer.add(a+b)
                currentAnswer.add(a-b)
                currentAnswer.add(a*b)
                if b != 0:
                    currentAnswer.add(Fr(a,b))

    #Don't forget the possibility of concatenating digits.
    currentAnswer.add(concat(range(start,stop+1))) 
    answers[(start,stop)] = currentAnswer
    return answers[(start,stop)]


rawAnswer = countPossibilities(1,SIZE)
sumz = 0
for ans in rawAnswer:
    if type(ans) == type(1):
        if ans > 0:
            sumz += ans
    elif ans.denominator == 1 and ans > 0:
        sumz += ans
print "The answer is:", sumz
print "Time Taken:", time.time() - START


"""
For this problem, I took a dynamic programming approach. I first calculated all the possible numbers from 1 to x, and x+1 to 9, then combined them. The only problem with this was that at each step, there was up to 4mn elements produced (m from 1 to x, n from x+1 to 9). This caused a bit of slowdown, but for 1 to 9, it was sufficiently fast.


Congratulations, the answer you gave to problem 259 is correct.

You are the 919th person to have solved this problem.

You have earned 1 new award:

Decimation II: Solve one in every ten problems from problems 201 to 300

The answer is: 20101196798
Time Taken: 312.511977911


"""
