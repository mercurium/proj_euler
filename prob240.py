import time
START = time.time()
from math import factorial as fa

numDie = 20
maxDieNum = 12
total = 70
topDice = 10

def countDie(minNum, dieNum, sumz,prod, numInRow):
    if minNum > maxDieNum or sumz > total:
        return 0
    if dieNum == numDie:
        if sumz == total:
            return fa(numDie)/prod /fa(numInRow)
        else:
            return 0
    if dieNum >= numDie-topDice:
        a = countDie(minNum, dieNum+1,sumz+minNum,prod,numInRow+1)
    else:
        a = countDie(minNum, dieNum+1,sumz,prod, numInRow+1)
    b = countDie(minNum+1,dieNum,sumz, prod*fa(numInRow),0)
    return a+b


print countDie(1,0,0,1,0)

print "Time Taken:", time.time() - START


"""
Congratulations, the answer you gave to problem 240 is correct.

You are the 1352nd person to have solved this problem.

Return to Problems page.

00:34 ~/Desktop/python_projects/proj_euler $ python prob240.py 
7448717393364181966
Time Taken: 88.1096231937 (using arrays and computing sum at end)
Time Taken: 71.6896748543 (computing sum as running total, saves space)


"""
