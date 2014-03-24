import time
start = time.time()

size = 10**6

vals = dict()
iterations = 0


for a in xrange(1,size):
    for b in xrange(a//4+1,a):
        n = a*(4*b-a)
        if n > size:
            break
        iterations +=1
        if n in vals:
            vals[n] +=1
        else:
            vals[n] = 1

print "Time Taken:", time.time() - start


count = 0
for i in xrange(1,size):
    if i in vals and vals[i] == 1:
        count +=1

print "count =", count
print "num of iterations= ", iterations
print "Time Taken:", time.time() - start

"""

~/Desktop/python_projects/proj_euler $python prob136.py
Time Taken: 112.820966005
count = 2544559
num of iterations=  118626576
Time Taken: 125.128010988

so wasteful in computations... only one in 46 or so mattered... T.T

"""

