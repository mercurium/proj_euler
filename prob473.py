import time, math
START = time.time()
SIZE = 10**10
GOLDEN_RATIO = (1+ 5**.5)/2

gr = GOLDEN_RATIO
baseRatio = gr**5 + gr**2
logSize = int( math.log(SIZE/baseRatio, gr)/2) +1

palindromes = [2] + [ int(baseRatio * gr**(2*i)+.3) for i in range(logSize)]

###Input arguments
#pal = integer array of numbers that are palindromes in base gr
#index = integer denoting index into pal
#sumz = double representing the cummulative sum of the palindrome thus far

### Output:
# The sum of all palindromes base GR that we can make with the given input palindromes
def countPalindromeSum(pal, index, sumz):
    if index == -1: #since we didn't include 14, we could either add 2, or not add 2
        return sumz  + (sumz+2)
    if index == -2:
        return sumz
    if index == -3: #redundant case
        return   0

    includeCurrentIndex = countPalindromeSum(pal, index-3, sumz+pal[index])
    dontIncludeCurrentIndex = countPalindromeSum(pal, index-1, sumz)
    return includeCurrentIndex + dontIncludeCurrentIndex

print countPalindromeSum(palindromes, len(palindromes)-1, 0) + 1
print "Time Taken:", time.time() - START

"""
So my first key insight for this problem was realizing that first off, since this is the golden ratio, if phi = x (for convenience sake), then we get:
    x^k = x^{k-1} + x^{k-2}
for all integers k.

After that, I made a simple routine that output all the palindromes under 10^4. Doing that, I noticed that all of the palindromes (excluding 1 and 2) outputted were either of the form:
100100(0 x (2i)), or a sum of different palindromes of that form. For example, we have:
14 = 100100.001001
36 = 10010000.00001001
94 = 1001000000.0000001001
and etc. After a while, the decimal part becomes negligible (really soon actually), and I just started rounding them, so I got

14 ~= 100100
36 ~= 10010000
94 ~= 1001000000
and so on.

Then, following that, it's pretty easy to generate all the palindromes of the form 100100(0 x 2i), and the last step is combining them together. Since we don't allow for powers to be used more than once, we can not use two palindromes that less than 3 apart (excluding the case where palindrome = 2). Therefore, we get the recurrence relation that I have in countPalindromeSum, and voila, out comes the answer.


Congratulations, the answer you gave to problem 473 is correct.

You are the 226th person to have solved this problem.

35856681704365
Time Taken: 0.00422191619873



I derped and forgot that since this is the golden ratio, we literally have
x^{k+2} = x^{k+1} + x^k

It looks like the numbers are of the form 100100(0x3)0x2. (same thing in reverse)

"""
