import time
from math import e, log
start = time.time()
size = 100

total_sum = 0;

for i in range(5,size+1):
  guess = int(i/e + .5)
  if i * (2**(int(log(size,2))) * 5**(int(log(size,5)))) % guess == 0:
    total_sum += i
  else: total_sum -= i
  
print total_sum

print "Time Taken: " + str(time.time()-start)
