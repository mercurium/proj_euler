import time, math
START = time.time()

vals      = dict()
repeatDig = 2

def knap(accumVal, index, numLeft):

  if (accumVal,index,numLeft) in vals:
    return vals[(accumVal, index, numLeft)]

  if numLeft == 0 and (accumVal - 1) % 11 == 0 and index == -1:
    return math.factorial(10) **2
  elif numLeft < 0 or index == -1:
    return 0

  if index == 0:
    vals[(accumVal, index, numLeft)] =  \
         knap(accumVal, index - 1, numLeft) / repeatDig + \
         knap(accumVal + index, index - 1, numLeft - 1) * 9 / 10 + \
         knap(accumVal + 2 * index, index - 1, numLeft - 2) * 2 / 5
    return vals[(accumVal, index, numLeft)]

  vals[(accumVal, index, numLeft)] =  \
         knap(accumVal, index - 1, numLeft) / repeatDig + \
         knap(accumVal + index, index - 1, numLeft - 1) + \
         knap(accumVal + 2 * index, index - 1, numLeft - 2) / repeatDig
  return vals[(accumVal, index, numLeft)]

print knap(0,9,10)

print "Time Taken:", time.time() - START


"""
Answer is  : 194505988824000
Time Taken : 0.00179719924927
You are the 106th person to have solved this problem.

1) For a number to be divisible by 11, the sum of the odd digits (10, 1,000, 10**5, etc) must be 0 mod 11 different from the sum of the even digits (1, 100, 10000, etc).

2) Then the number of numbers that are double pandigital is the number of permutations of the digits such that the odd digits are equal to the even digits mod 11.

3) For a given distribution of digits to the odd/even groups, there are (10!)^2 ways of arranging them. However, if a digit is repeated, then half of the permutations are identical, so we need to divide by 2.

4) For the case of leading zeros, we need to remove all cases which have leading zeros. For the odd digit set, this is approximately 1/10 of them when 1 of the digits is a 0, 2/10 of them when 2 of the digits are 0, and 0/10 if none of the odd digits are 0. This gives us the multipliers 1x, 9/10x, and 4/5x.

5) Combining 3) and 4), the multipliers for the 0 digits gives us 1/2, 9/10, and 2/5.

Plugging in the parameters, we get our final answer of 194505988824000.

The reason I called my function 'knap' is because this is similar to the knapsack question, where you either pick a digit to be in a digit group, or you don't. This was quite a fun problem, and I'm saddened that I didn't finish it faster. Seriously though, someone did this in 4 min. wtf...


"""
