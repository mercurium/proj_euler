import string
import math
import time
START = time.time()

#50000, 10000 are arbitrary numbers, just initial numbers to see if we can find the answer within that amount. If not, increase them.
pentagon_set = set( [ (i * (3*i-1)/2) for i in range(1,50000) ] )  
penta_lst = [ i * (3*i-1)/2 for i in xrange(10000)]

done = False
for i in xrange(2,10000):
    a = penta_lst[i] 
    for j in xrange(1,i):
        b = penta_lst[j] 
        if a+b in pentagon_set and a-b in pentagon_set:
            print a-b, a, b, a+b, '\n', i,j
            done = True
            break
    if done:
        break


print "The answer is:", a-b
print "Time Taken:", time.time()-START

"""
12:28 ~/Desktop/python_projects/proj_euler $ python prob45.py 
answer is: 1533776805
Time taken: 0.0236649513245
"""
