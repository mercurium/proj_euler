import time
start = time.time()

#we're going to start at n = 3

old = [1,0,0,1]
new = [0,0,0,0]

for i in xrange(4,51):
  new[0] = old[0] + old[3]
  new[1] = old[0]
  new[2] = old[1]
  new[3] = old[2] + old[3]
  old = new[:]

print sum(old)
print "Time Taken: ", time.time() - start
"""
~/Desktop/python_projects/proj_euler $python prob114.py
16475640049
Time Taken:  0.000109910964966


Okay, so this problem stumped me for a really long time. So what I realized was this: if you have to have chains at least k long, then that means that you only care about the last k numbers in the f(n-1) case, with basecase f(k) = 2 and f(a) = 1 for a < k.

So for the case of k = 3, the four possible endings for a chain are
BBB
RBB
RRB
BBB

Of these, we can append a B to them to make a chain of length n+1, but for some of them we can append an R to the end. The only obvious one which we can append to is the RRR case. However, if we have the BBB case, we can turn it into BRRR without repeating a case. Since BRR is not covered in our tail cases, we have created a new result.

Proof for why this generates all results: If we had a case where we couldn't get from this, then the tail would have to be one of BBBB, RBBB, RRBB, RRRB, RRRR, BRRR. We have generated all cases of BBBB, RBBB, RRBB, and RRRB by merely appending a B to a previously valid chain of length (n-1). The last case, BRRR, is generated from having BBBB and flipping it into BRRR. Since BRR is not a valid chain ending, it could not have been generated from previous chains. Thus we have found all possible solutions.

"""
