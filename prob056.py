import string, time
START = time.time()

def count_dig(n):
    return sum([int(dig) for dig in str(n)])

maxVal = 0
maxA, maxB = 0,0
for a in range(50,100):
    for b in range(50,100):
        n = a**b
        mn = count_dig(n)
        if maxVal < mn:
            maxVal = mn
            maxA,maxB = a,b
print maxVal, maxA,maxB
print "Time Taken:", time.time() - START
