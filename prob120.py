import time
startz = time.time()
sumz = 0
for i in range(3,1001):
  if i%2 == 0:
    sumz += i*i-2*i
  else:
    sumz += i*i-i
print sumz


print "Time Taken: " + str(time.time()-startz)
