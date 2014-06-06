"""
This is my old code that I'm a bit reluctant to throw away since it's.... kinda cool for me to look back on xD

Please forgive me for my unclean code here :P

"""


import time, math
START = time.time()
SIZE = 10**3
GOLDEN_RATIO = (1+ 5**.5)/2
TOLERANCE = 10**-6
ARR_SIZE = 100

def testPalindrome(n): #int n
    powerArr = [0]*ARR_SIZE
    while n > TOLERANCE:
        powerIndex = math.log(n, GOLDEN_RATIO)
        if powerIndex < int(powerIndex) - TOLERANCE:
            #print powerIndex, int(powerIndex)
            powerIndex = int(powerIndex)-1
        else:
            powerIndex = int(powerIndex)
        if powerIndex < -20:
            #print powerIndex
            break
        powerArr[powerIndex] +=1
        n -= GOLDEN_RATIO**powerIndex
    #print powerArr
    return powerArr == powerArr[::-1]

gr = GOLDEN_RATIO
palindromes = [2] + [ int((gr**5+gr**2) * gr**(2*i)+.3) for i in range(22)]
print palindromes

memoize = dict()
def countPalindromeSum(pal, index, sumz):
    if index in memoize:
        return memoize[index]
    if index == -2:
        #print sumz, "-2"
        return sumz
    if index == -1:
        #print sumz +2, "-1"
        #print sumz, "-1"
        return sumz * 2 + 2
    if index < 0:
        return 0

    route1 = countPalindromeSum(pal, index-3, sumz+pal[index])
    route2 = countPalindromeSum(pal, index-1, sumz)
    return route1+route2

print countPalindromeSum(palindromes, len(palindromes)-1, 0) + 1

palindromes = set([1])
lst = [0] * ARR_SIZE

#for j in range(1,SIZE+1):
#    lst[0] += 1
#    contin = True
#    while contin:
#        contin = False
#        for i in range(-len(lst)/2,len(lst)/2):
#            if lst[i] == 2:
#                lst[i+1] +=1
#                lst[i-2] +=1
#                lst[i] -= 2
#                contin = True
#            if lst[i] == lst[i+1] == 1:
#                lst[i] = 0
#                lst[i+1] = 0
#                lst[i+2] +=1
#                contin = True
#    if lst == lst[::-1]:
#        palindromes.add(j)
#        print j, '\t', sum([10**x * lst[x] for x in range(len(lst)/2)])
#
#
#print '\n', sum(palindromes)
print "Time Taken:", time.time() - START



"""
Congratulations, the answer you gave to problem 473 is correct.

You are the 226th person to have solved this problem.

1   1
2   10.01
3   100.01
4   101.01
5   1000.1001
6   1010.0001
14  100100.001001

2 14 36 38 94 96 246 248 260 644 646 658 680 682 1686 1688 1700 1722 1724 1780 1782 4414 4416 4428 4450 4452 4508 4510 4660 4674

I derped and forgot that since this is the golden ratio, we literally have
x^{k+2} = x^{k+1} + x^k

It looks like the numbers are of the form 100100(0x3)0x2. (same thing in reverse)

"""
