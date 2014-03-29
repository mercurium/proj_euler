#NOTE TODO need to solve it
import time, random
START = time.time()

numIter = 10**6 * 5
count = 0
for iteration in range(numIter):
    L = []
    R = []
    for i in range(50):
        tempCount = 0
        randNum = random.randint(1,10)
        if randNum in L:
            tempCount +=1
            a = L.index(randNum)
            del L[a]
        else:
            if len(L) == 5:
                L.pop(0)
        L.append(randNum)
        if randNum in R:
            tempCount -=1
        else:
            if len(R) == 5:
                R.pop(0)
            R.append(randNum)
    count += abs(tempCount)
print count*1.0/numIter
print "Time Taken:", time.time() - START
