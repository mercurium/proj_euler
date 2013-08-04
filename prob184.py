import time
start = time.time()
import sys

if len(sys.argv) > 1:
	R = int(sys.argv[1])
else:
	R = 25

points = set()
for x in xrange(-1 * R + 1, R):
	for y in xrange(-1*R+1,R): #this could be optimized,but not worth it... 
		if x**2+y**2 < R**2:
			points.add((x,y))
points.remove((0,0))

set1 = set() #points above the x axis
set2 = set() #points below the x axis
for point in points:
	if point[1] > 0:
		set1.add(point) 
	elif point[1] < 0:
		set2.add(point)
	elif point[0] > 0:
		set1.add(point)
	else:
		set2.add(point)
#Because the thing is symmetrical, we only need to do it for half of the points, not both sets... =D 

count = 0
set1 = list(set1)
for i in range(len(set1)):
	point = set1[i]
	above = 0
	below = 0
	for btm_pt in set2:
		val = btm_pt[0] * point[1] - btm_pt[1] * point[0]
		if val > 0:
			above +=1
		elif val < 0:
			below +=1
	count += above * below	

print count*2
print "Time Taken:", time.time() - start

"""
Congratulations, the answer you gave to problem 184 is correct.

You are the 796th person to have solved this problem.

Nice work, mercurium, you've just advanced to Level 8.
1144 members (0.35%) have made it this far.


1725323624056
Time Taken: 112.400161982

LOL SOOOO... the irony is that I've already solved this problem a long while back when I was applying for internships. Vivek from Hackerrank had me solve it as an interview question and I typed up the solution for it... sooo... the pretty solution is already there typed up... 
"""
