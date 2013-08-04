import math
import time
start = time.time()

size = 10**9
plst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

ham_set = set([ 97**i for i in xrange(0,int(math.log(size,97) +1)) ])
for i in xrange(len(plst)-2,-1,-1):
	print plst[i], len(ham_set)
	print "Time Taken:", time.time() - start
	old_lst = list(ham_set)
	old_lst.sort()
	val = plst[i]
	for k in xrange(1, int(math.log(size, plst[i]) +1)):
		for j in old_lst:
			valz = j * val
			if valz > size: break
			ham_set.add(valz)
		val *= plst[i]

print len(ham_set)
print "Time Taken:", time.time() - start

#hehe, this is a list of the speed increases I've been having~ <3
#2944730
#Time Taken: 56.2888171673 original speed
#Time Taken: 21.3924460411 changed the order of the loops a bit
#Time Taken: 4.95116686821 started adding to the set from 97 instead of 2
#Time Taken: 4.26534819603 added the break after val > size
#Time Taken: 4.00025296211 kept a counter of val^k
#Time Taken: 2.02729320526 for using desktop... LOL T.T
