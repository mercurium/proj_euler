import time
start = time.time()
import sys

size = int(sys.argv[1])
num_iter = int(sys.argv[2])

def main():
	x = [(2*k*(size-k+1)-1)/size**2. for k in xrange(1,size/2+1)]

	results = 0
	ncrd = 1.

	for i in xrange(0,num_iter+1,2):
		temp = 0
		for j in xrange(0,size/2):
			temp += x[j]**i * (1-x[j])**(num_iter-i)
		results += temp * ncrd
		ncrd = (ncrd * (num_iter-i) * (num_iter-i-1)) / ((i+1) * (i+2))

	print results*2
	print "Time Taken:", time.time() - start

main()

print
