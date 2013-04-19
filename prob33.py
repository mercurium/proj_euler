import time
start = time.time()



for i in range(1,10):
  for j in range(1,10):
    for k in range(1,10):
      if (10. * i + j)/(10*j + k) == i*1.0/k and i != k:
        print i,j,k
         
print "Time Taken: " + str(time.time()-start)
