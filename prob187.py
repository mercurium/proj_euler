import math
import time
start = time.time()


return 0


n2 = 3001134
n3 = 2050943
n5 = 1270607
n7 = 927432
n11= 608113
n13= 520415
n17= 405279
n19= 365552

size = 10**7/2
primes = [0] * 348513
sumz = n2+n3+n5+n7+n11+n13+n17+n19
if True:
  #here's the actual start of the program
    start = time.time()
    lst = [0]*size

    count = 0
    for i in range(2,len(lst)):
      if lst[i] == 0:
        for j in range(i, len(lst), i):
          lst[j] += 1
        primes[count] = i
        count += 1
    
    print "Time Taken: " + str(time.time()-start)
    primes = primes[9:]
    for i in range(0,len(primes)):
      if primes[i] > 10**4:
        break
      est = size * 20.0/ primes[i]
      p_fac = int(est/math.log(est) *1.1)
      for j in range(p_fac,-1,-1):
        if primes[j] * primes[i] < 10**8:
          sumz+= j
          break


    print "Total number: ",sumz

print "Time Taken: " + str(time.time()-start)
