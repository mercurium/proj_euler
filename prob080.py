import time
from math import log

START = time.time()
SIZE = 100
sq = [x**2 for x in range(1,int(SIZE**.5))]

def calc(m):
    goalValue = m * 10**200
    currentDiff = goalValue
    sumz = int(m**.5)*10**100
    errorFixDig = -1
    for i in xrange(99,-1,-1):
        for dig in xrange(0,10):
            num = sumz + dig * 10**i
            if num**2 > goalValue:
                break
            if goalValue - num**2 <= currentDiff:
                currentDiff = goalValue - num**2
                errorFixDig = dig
        sumz += errorFixDig * 10**i
    return sumz
    

sumz = 0
for i in xrange(2,100):
    if i not in sq:
        sumz += sum([int(x) for x in str(calc(i))[:100]])

print sumz
print "Time Taken: ", time.time() - START

"""
~/Desktop/python_projects/proj_euler $python -i prob80.py
40886
Time Taken:    0.280507087708 (on desktop)

Method of attack: Since floats have limited precision, I went with the method of multiplying everything by 10^100 to turn the first 100 digits into integers. Then I went digit by digit and checked out which one gave the best result.

Considering that there were 100 digits, each of which had 10 possible choices, and we were comparing 200 digit numbers, we had to do at most 1000 squarings per number we checked, and we did this 90 times (1-100 excluding squares). This comes out to a max of 1000*100 = 100,000 squarings. However, of course we don't always go for all 10 checks, therefore (on average) we only needed to check 5 possibilities for 10 numbers, the actual required computation probably came out to ~50,000 squarings. Seeing how we add 1 to our total count every time we do this (and one more per digit per number that is unseen), the fact that we get 40,886, which is approximately 10000 less than 50000 is not a surprise.

"""







