import time, math, string
START          = time.time()
SIZE           = 10**14
MOD            = 11111**2
TEN_REPEAT_NUM = 55555 # 10^55555 = 1 mod 11111^2

repeatNumLst = [1,2,3,4,3,2]
repeatNum    = '123432'

def lstToInt(lst):
    if len(lst) == 0:
        return 0
    return int(string.join([str(x) for x in lst], ''))

def getSmallClockSeq():
    smalls = [None] * 15
    index = 0
    for i in xrange(15):
        nums  = []
        while sum(nums) < i:
            nums.append(repeatNumLst[index % 6])
            index += 1
        smalls[i] = nums

    return smalls

smalls = getSmallClockSeq()

def getOffsetRepeat(n):
    n     = n % 15
    index = (repeatNum * 2).index(string.join([str(x) for x in smalls[n]], ''))

    return repeatNumLst[index:] + repeatNumLst[:index]

def getClockSeq(n):
    if n < 15:
        return smalls[n]

    numRepeat = n // 15
    repeatSeq = getOffsetRepeat(n)

    return repeatSeq * numRepeat + smalls[n % 15]

def clockSeqInt(n):
    return lstToInt(getClockSeq(n))

csi = clockSeqInt

def getMidMultiplier(numRepeat, numDigTail):
    return sum([ \
        pow(10, 6*dig + numDigTail, MOD) \
        for dig in xrange(numRepeat) \
    ])

def computeClockSeqMod(n):
    tail   = smalls[n%15]
    mid    = getOffsetRepeat(n)

    numRepeatMid = n / 15
    numDigTail   = len(tail)

    sumz = lstToInt(tail) \
            + lstToInt(mid) * getMidMultiplier(numRepeatMid, numDigTail)
    return sumz % MOD

def getMidMultMany(numRepeat, numDigTail):
    multiplier = 0
    for dig in xrange(min(numRepeat, TEN_REPEAT_NUM)):
        numTimes = (numRepeat - dig) / TEN_REPEAT_NUM + 1
        tenMult  = numTimes * ((numRepeat - dig) % TEN_REPEAT_NUM) \
                    + numTimes * (numTimes - 1)/2 * TEN_REPEAT_NUM
        multiplier += tenMult * pow(10, 6*dig + numDigTail, MOD)
    return multiplier

# computes sum of numbers equal to n % 15 and <= n
def computeClockSeqModMany(n):
    tail = smalls[n%15]
    mid  = getOffsetRepeat(n)

    numRepMid  = n / 15
    numDigTail = len(tail)

    sumz = lstToInt(tail) * (numRepMid + 1) \
            + lstToInt(mid) * getMidMultMany(numRepMid, numDigTail)
    return sumz % MOD


def computeClockSum(n):
    if n < 15:
        return sum(smalls[:n+1])

    sumz = 0
    for i in xrange(SIZE,SIZE-15,-1):
        sumz += computeClockSeqModMany(i)
    return sumz % MOD



answer = computeClockSum(SIZE)
print "Answer:", answer

print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 506 is correct.

You are the 513th person to have solved this problem.

Answer: 18934502
Time Taken: 0.755791187286

This problem is pretty simple actually. Since 1+2+3+4+3+2 = 15, any number > 15 is equal to:
(1,2,3,4,3,2 shifted around) * (n/15) + seq(n % 15)

Ex: seq(8) = 2123
seq(23 = 8+15)   =        212343 2123
seq(38 = 8+15*2) = 212343 212343 2123

So computing each number is simple. Beyond that, summing them up is just adding similar numbers.

Given that 10^55555 = 1 mod 11111^2, we repeat our numbers after a while and it makes it an O(1) adding operation rather than O(n).

I'm leaving a few extra methods around, though they aren't necessary for solving the problem because they help generate valeus for this problem

"""
