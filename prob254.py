import time
START = time.time()
from math import factorial as fa
import string

min_val = dict()
SIZE = 150

def f(n):
    return sum([fa(int(i)) for i in str(n)])

def sf(n):
    return sum([int(i) for i in str(f(n))])

def g(n):
    if n in min_val:
        return min_val[n]
    valz = 0
    lim = max([0] + [min_val[x] for x in min_val]) 
    while valz != n:
        lim +=1
        test = str(lim)
        if len(test) > 4 and (ord(test[0]) > ord(test[1]) or ord(test[1])> ord(test[2]) or ord(test[2]) > ord(test[3]) or ord(test[3]) > ord(test[4]) ):
            lim += 10**(len(test)-5)
            continue
        if len(test) > 6 and (ord(test[4]) > ord(test[5]) or ord(test[5]) > ord(test[6]) ):
            lim += 10**(len(test)-7)
            continue

        valz = sf(lim)

        if valz not in min_val:
            min_val[valz] = lim
        if lim %65536== 0:
            print "RAAAH", lim, n
    return lim

def sg(n):
    ans = g(n)
    return sum( [int(i) for i in str(ans)]),ans

lim = 1
sumz = 0
for i in range(1,SIZE+1):
    ans, next_val = sg(i)
    print i, ans, next_val
    sumz += ans
print sumz

print "Time Taken:", time.time() - START

"""
My current approach isn't working... it's not worth it to run it on this problem iteratively brute focring... should find better solution...

These are the solutions for 1 to 46:
{1: 1, 2: 2, 3: 5, 4: 15, 5: 25, 6: 3, 7: 13, 8: 23, 9: 6, 10: 16, 11: 26, 12: 44, 13: 144, 14: 256, 15: 36, 16: 136, 17: 236, 18: 67, 19: 167, 20: 267, 21: 349, 22: 1349, 23: 2349, 24: 49, 25: 149, 26: 249, 27: 9, 28: 19, 29: 29, 30: 129, 31: 229, 32: 1229, 33: 39, 34: 139, 35: 239, 36: 1239, 37: 13339, 38: 113599, 39: 4479, 40: 14479, 41: 2355679, 42: 344479, 43: 1344479, 44: 2378889, 45: 12378889, 46: 133378889}


"""
