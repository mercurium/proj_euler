import time
start = time.time()
from Queue import PriorityQueue as pq

items = pq()
items.put( (0,-1,{1}) )
SIZE = 200
vals = [3000] * (SIZE+1)
vals[0] = 0

while 3000 in vals:
	item = items.get()
	priority = item[0]
	new_priority = priority+1 
	old_val = -1*item[1] # reason for making it negative is due to
	elem = item[2]      #implementation of priority queue. Takes smallest first.
	if old_val > SIZE:
		continue

	if vals[old_val] > priority:
		vals[old_val] = priority

	for i in elem:
		new_val = i+old_val
		if new_val > SIZE or vals[new_val] != 3000:
			continue 
		new_set = set(list(elem))
		new_set.add(new_val)
	 	items.put( (new_priority,-1*new_val,new_set) )
print sum(vals)
print "Time Taken: " + str(time.time()-start)

"""
Congratulations, the answer you gave to problem 122 is correct.

You are the 3600th person to have solved this problem.

11:08 ~/Desktop/python_projects/proj_euler $ python prob122.py 
1582
Time Taken: 0.256936073303
"""
