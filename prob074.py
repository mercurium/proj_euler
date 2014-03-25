import time, math
START = time.time()

SIZE = 10**6
chainCount = [-1]*(10**7+1)

def factSum(n):
    runningSum = 0
    while n != 0:
        runningSum += math.factorial(n%10)
        n/=10
    return runningSum

def getCount(i):
    if chainCount[i] == -1:
        chainCount[i] = 0 #for initializing and stopping recursive calls
        chainCount[i] = 1 + getCount(factSum(i))
    return chainCount[i]

sumz = sum([ (getCount(i) == 60) for i in range(1,SIZE)])

print sumz
print "Time Taken:", time.time() - START
    
