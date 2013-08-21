import time
START = time.time()

for i in xrange(166,10**5): #Starting at 166 since we want the next one past 165
	n = i*(3*i-1)/2 # The pentagonal number
	m = int((n/2)**.5+1)  #Getting what the m would be if this were a hexagonal number
	if m*(2*m-1) == n: #Checking that the m computed is actually for a hexagonal numbe = n
		print "answer is:", n
		break

print "Time taken:",time.time() -START

"""
Since all hexagonal numbers are also triangle numbers, we only need to find out when the next hexagonal-pentagon number occurs.


12:00 ~/Desktop/python_projects/proj_euler $ python prob45.py 
answer is: 1533776805
Time taken: 0.0246548652649
"""
