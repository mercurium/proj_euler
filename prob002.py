import time
START = time.time()

SIZE = 4*10**6
a,b = 1,1
sumz = 0
while a <SIZE:
	a,b = b,a+b
	if a % 2 == 0:
		sumz+= a
print sumz
print "Time Taken:", time.time()-START 

"""
[tw-mbp13-jerrychen proj_euler (master)]$ python prob2.py 
4613732
Time Taken: 0.000344038009644

Pretty simple exercise, just get the next fibonnaci number at each step, if it's even, add it to the sum. Stop the loop when you hit thelimit 
"""


