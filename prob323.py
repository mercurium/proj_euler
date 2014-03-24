import time
from math import factorial as fa
START = time.time()


def ncr(n,r):
    return fa(n)/(fa(r) * fa(n-r))


x_n = [0]*33


#The ncr/pow(2.,i) is the probability of getting a number that gets rid of j of the digits, and then we have i-j digits left to remove, which we know is x_n[i-j]
for i in range(1,len(x_n)):
    sumz = 0
    for j in range(0,i+1):
        sumz += ncr(i,j) *(x_n[j]+1) / pow(2.,i) 
    x_n[i] = sumz * pow(2.,i) / (pow(2.,i) -1.)
print x_n[32]
print "time elapsed", time.time() - START 



"""

~/Desktop/python_projects/proj_euler $python prob323.py
6.3551758451
time elapsed = 0.003093957901


Okay, this problem was pretty easy as is. The thing that we note that if we get rid of 15 digits out of 32, we've pretty much reduced that problem to finding out the expected number of numbers required to clear off 17 digits + 1 more for removing the first 15 digits. Thus we can do this problem recursively using DP for win.

Main point is, we expand on

E[2] = 1/4(E[0]+1) + 1/2(E[1] + 1) + 1/4(E[2] +1)

"""
