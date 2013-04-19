import time
start = time.time()
from math import *
fa = factorial
from primes import factor


def log10(n):
    return log(n) / log(10)


def sum10(abc):
    sumz = 10 ** (abc[0] / log_err)
    sumz += 10 ** (abc[1] / log_err)
    return sumz + 10 ** (abc[2] / log_err)

size = 2 * 3 * 5 * 7 * 11
log_err = 1000.
vals = factor(size)[:-1]

vals = [int(log_err * log10(val)) for val in vals]
total = sum(vals)
prev = {}
min_val = [10 ** 20]


def helper(a, b, c, pos):

    if sum10((a, b, c)) > min_val[0]:
        return (float('inf'), float('inf'), float('inf'))

    #end of array
    if pos == len(vals):
        if sum10((a, b, c)) < min_val[0]:
            min_val[0] = sum10([a, b, c])
        return (a, b, c)

    #if we've seen it before...
    if (a, b, c, pos) in prev:
        return prev[(a, b, c, pos)]

    an = helper(a + vals[pos], b, c, pos + 1)
    bn = helper(a, b + vals[pos], c, pos + 1)
    cn = helper(a, b, c + vals[pos], pos + 1)

    if sum10(an) <= sum10(bn) and sum10(an) <= sum10(cn):
        prev[(a, b, c, pos)] = an
    elif sum10(bn) <= sum10(an) and sum10(bn) <= sum10(cn):
        prev[(a, b, c, pos)] = bn
    else:
        prev[(a, b, c, pos)] = cn
    return prev[(a, b, c, pos)]

ans = [int(10 ** (a / log_err) + .5) for a in helper(0, 0, 0, 0)]
print ans, sum(ans)


print "Time Taken:", time.time() - start


"""

This is the answer with a huge error in approximation... lol
~/Desktop/python_projects/proj_euler $python prob418.py
[398107170553498560, 398107170553498560, 398107170553498560] 1194321511660495680
Time Taken: 6.07174706459

"""
