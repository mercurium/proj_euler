import time
start = time.time()
from m_rTest import m_r

def sum_dig(n):
    sumz = n%10
    while n!= 0:
        n/=10
        sumz += n%10
    return sumz

harshad = dict()
harshad[1] = {1,2,3,4,5,6,7,8,9}
for i in range(2,15):
    harshad[i] = set()

for j in xrange(1,14):
    for n in harshad[j]:
        num = n*10
        for dig in xrange(10):
            if (num+dig)%sum_dig(num+dig) == 0:
                harshad[j+1].add(num+dig)


sumz = 0
for i in range(1,14):
    for j in harshad[i]:
        a = sum_dig(j)
        if j% a == 0 and m_r(j/a):
            if m_r(j*10+1): 
                sumz+=j*10+1
            if m_r(j*10+3): 
                sumz+=j*10+3
            if m_r(j*10+7): 
                sumz+=j*10+7
            if m_r(j*10+9): 
                sumz+=j*10+9


print sumz
print "Time Taken:", time.time()-start


"""
~/Desktop/python_projects/proj_euler $python prob387.py
696067597313468
Time Taken: 0.834525108337

Simple problem. Just scaffold you way up, find strong right trunckatable numbers, then test the possible primes that you can build off of that.

Rofl. of the .83 seconds that my program takes, .5 of it was to build the set of primes for the miller_rabin primality tests... :/
"""
