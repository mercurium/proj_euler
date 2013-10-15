import time,random
START = time.time()


count = 0
SIZE = 10**7
for iteration in xrange(SIZE):
	s1,s2 = 0,0
	n1 = random.random()
	while s1 < 1:
		s1 += n1
		n1 = random.random()
	n2 = random.random()
	while s2 < 2:
		s2 += n2
		n2 = random.random()
	if n1 < n2:
		count +=1


print "Out of", SIZE, "rounds, player 2 won:", count 
print "Time Taken:", time.time() - START
