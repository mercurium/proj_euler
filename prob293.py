import time
start = time.time()
from math import log
from primes import m_r

SIZE = 10**9
primes = [2,3,5,7,11,13,17,19,23]
old_set = set([1])
new_set = set()
admiss_set = set()
for p in primes:
    for j in xrange(1,int(log(SIZE,p)+1) ):
        p_pow = p**j
        for item in old_set:
            if item * p_pow < SIZE:
                new_set.add(item*p_pow)

    for item in old_set:
        admiss_set.add(item)
    old_set = new_set
    new_set = set()

for item in old_set:
    admiss_set.add(item)
admiss_set.remove(1)
print len(admiss_set), "is how many admissible numbers we need to deal with,"
print "Time Taken:", time.time() - start

######################################### Above this is finding admissible numbers

fort_num = set() # the pseudo-fortunate numbers

for num in admiss_set:
    n = num+2
    while not m_r(n):
        n += 1
    fort_num.add(n-num)

print sum(fort_num), "is our final answer"
print "Time Taken:", time.time() - start

"""
Congratulations, the answer you gave to problem 293 is correct.

You are the 1292nd person to have solved this problem.

22:17 ~/Desktop/python_projects/proj_euler $ python prob293.py 
6656 is how many admissible numbers we need to deal with,
Time Taken: 0.0592079162598
2209 is our final answer
Time Taken: 0.359772920609

"""





