import time
start = time.time()

SIZE = 10**6
vals = dict()

for x in xrange(3,SIZE/4 + 2):
	a = x**2
	loop_start = x**2 - SIZE
	if loop_start <= 1:
		loop_start = 1
	else:
		loop_start = int(loop_start**.5)
	if (loop_start + x) %2 == 1:
		loop_start +=1


	for y in xrange(loop_start,x-1,2):
		value = a - y**2
		if y == 0 or value > SIZE or value <= 0: 
			continue
		if value in vals:
			vals[value] +=1
		else:
			vals[value] = 1

count = dict()

for i in xrange(30):
	count[i] = 0

for i in vals:
	if vals[i] < 30:
		count[vals[i]] +=1

print "Testing the value of count[15], should be 832, actually is:", count[15]

print sum([count[x] for x in xrange(1,11)]), "Is the answer "
print "Time Taken:", time.time() - start


"""
02:18 ~/Desktop/python_projects/proj_euler $ python prob174.py 
Testing the value of count[15], should be 832, actually is: 832
209566 Is the answer 
Time Taken: 1.34566688538

Congratulations, the answer you gave to problem 174 is correct.

You are the 3129th person to have solved this problem.

Return to Problems page.

Since we have a laminae as the difference between two squares, we just need to find all sets x^2 - y^2 = N, which is not hard. In addition, x^2 - y^2 = (x+y)(x-y), which means that y < x and that if x > N/4+1, we've gone too far. Finally, since the inner square is centered with the outer square at the same point, they have to have the same parity in side lengths, so we  have

y <= x-2.
"""
