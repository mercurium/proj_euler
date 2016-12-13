import time
start = time.time()
import sys

num_iter = int(sys.argv[2])
size = int(sys.argv[1])

def main():
  x = [(2*k*(size-k+1)-1)/size**2. for k in xrange(1,size+1)]

  results = [0] *size
  ncrd = 1.

  for i in xrange(0,num_iter+1,2):

    for j in xrange(0,size):
      results[j] +=ncrd * x[j]**i * (1-x[j])**(num_iter-i)
    ncrd = (ncrd * (num_iter-i) * (num_iter-i-1)) / ((i+1) * (i+2))

  print sum(results)
  print "Time Taken:", time.time() - start

main()

print
