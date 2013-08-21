import time
START = time.time()

MOD = 10**10
sumz = 0 
for i in xrange(1,1001):
	sumz = sumz + pow(i,i, MOD)
	
print sumz % MOD
print "Time taken:",time.time() -START


"""
12:33 ~/Desktop/python_projects/proj_euler $ python prob48.py
9110846700
Time taken: 0.00292992591858

Lol, using my previous repeated squaring method... I had 
12:30 ~/Desktop/python_projects/proj_euler $ python prob48.py
9110846700
Time taken: 0.0142669677734

...7x slower using it.. :[
"""
