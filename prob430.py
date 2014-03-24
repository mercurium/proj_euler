import time
start = time.time()
import sys

SIZE = int(sys.argv[1])
NUM_ITER = int(sys.argv[2])

def main():
	prob = [(2*k*(SIZE-k+1)-1)/SIZE**2. for k in xrange(1,SIZE/2+1)]

	results = 0
	ncrd = 1.

	for i in xrange(0,NUM_ITER+1,2):
		temp = 0
		for j in xrange(0,SIZE/2):
			temp += prob[j]**i * (1-prob[j])**(NUM_ITER-i)
		results += temp * ncrd
		ncrd = (ncrd * (NUM_ITER-i) * (NUM_ITER-i-1)) / ((i+1) * (i+2))

	print results*2
	print "Time Taken:", time.time() - start

main()

print

"""
Note, this doesn't work for odd N because I wanted to save computation by halving the size. Since the problem asks for an even input, there's no reason to generalize the code when it just causes a slowdown in speed.

"""
