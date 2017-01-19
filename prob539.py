import time, math
START = time.time()
SIZE  = 2**5

def getLastElement(n):
    lst = range(1,n+1)
    while len(lst) > 1:
        lst = lst[1::2][::-1]
    return lst[0]

"""
1
8
8
64
64
256
256


"""
# 2**6  -> 2**8
# 2**7  -> 2**9
# 2**8  -> 2**11
# 2**9  -> 2**12
# 2**10 -> 2**14
# 2**11 -> 2**15
# 2**12 -> 2**17
def compute(n):
    val = 2**1

results = [-1]
numSum    = 0
valDict = dict()
for i in xrange(1, SIZE+1):
    lastElem = getLastElement(i)
    if lastElem in valDict:
        valDict[lastElem].append(i)
    else:
        valDict[lastElem] = [i]
    numSum += lastElem
    print i, '\t', lastElem

print numSum
print "Time Taken:", time.time() - START

"""
2^n
2^n - 2^1
2^n - 2^3
2^n - 2^3 - 2^1
2^n - 2^5 - 2^1
2^n - 2^5 - 2^3
2^n - 2^5 - 2^3 - 2^1
2^n - 2^7
2^n - 2^7  - 2^1
2^n - 2^7  - 2^3
2^n - 2^7  - 2^3 - 2^1
2^n - 2^7  - 2^5 - 2^1
2^n - 2^7  - 2^5 - 2^3
2^n - 2^7  - 2^5 - 2^3 - 2^1




"""
