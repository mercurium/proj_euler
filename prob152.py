from primes import factor
import time

START    = time.time()
MAX_SIZE = 81

numToExclude = set([11,16,17,19,22,23,25,26,27,29,31,32,33,34,37,38,41,43,44,46,47,48,49,50,51,53,55,57,58,59,61,62,64,65,66,67,68,69,71,73,74,75,76,77,78,79,80])

inverse      = [0,0] + [1./x**2 for x in range(2,MAX_SIZE+1)]

# This value is useful for figuring out how much more we could possibly add.
partial_sums = [inverse[-1]]
for i in xrange(MAX_SIZE):
    partial_sums.append(partial_sums[-1] + inverse[MAX_SIZE-i-1])
partial_sums = partial_sums[::-1]

used = set([2,3])

def recurse(n,num,denom, result=[]):
    if num * 2 == denom:
        print int(denom**.5), factor(int(denom**.5)), n-1
        print '\t\t', result
        used.update(set(result))
        return 1
    elif num*2 > denom or n > MAX_SIZE or num*1./denom + partial_sums[n] < .4999999:
        return 0
    while n in numToExclude:
        n+=1
    if n > MAX_SIZE:
        return 0


    if denom % n**2 == 0:
        b = recurse(n+1, num+denom/n**2, denom, result + [n])
    else:
        b = recurse(n+1, num*n**2+denom, denom*n**2, result + [n])

    a = recurse(n+1,num,denom, result)

    return a+b

print recurse(2, 0, 1)
print sorted(used)
print "Time Taken:", time.time() - START

"""
Answer: 301
Time Taken: 16.7504110336

Congratulations, the answer you gave to problem 152 is correct.

You are the 1783rd person to have solved the problem.

Okay, for this problem, there's some numbers that we know can't be part of the denominator, since there's not enough of that number's multiple to cancel out that factor in the denominator. Ex: if 1/53^2 is used, the resulting sum's denominator will be divisible by 53 since there's no other multiples of 53 to cancel it out.

This lets us remove:
  41,43,47,53,59,61,67,71,73,79 off the bat

Looking at numbers that won't have enough even with a multiple lets us remove even more numbers from consideration:
11,16,17,19,22,23,25,26,27,29,31,32,33,34,37,38,41,43,44,46,47,48,49,50,51,53,55,57,58,59,61,62,64,65,66,67,68,69,71,73,74,75,76,77,78,79,80

Once we've removed all those numbers, we get a much faster way to try out all combinations of the remaining numbers. Thus we can iterate through the reduced set much faster.


Example of cancelling out the denominator:


1/13^2 + 1/39^2 + 1/52^2 
= (1/13^2) * (1 + 1/3^2 + 1/4^2)
= (1/13^2) * (144/144 + 16/144 + 25/144)
= (1/13^2) * (169/144)
= 1/144, which is much easier to cancel out otherwise since 144 = 2^4 * 3^2

Forming 13:
  1,3,4

"""


