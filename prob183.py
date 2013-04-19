import time
from math import e, log
start = time.time()
size = 10000
size2 = 2**(int(log(size,2)))
size5 = 5**(int(log(size,5)))
size10 = size2 * size5
total_sum = 0;


for i in range(5,size+1):
    guess = int(i/e+.5)
    if i * size10 % guess == 0: total_sum -= i
    else: total_sum += i
print total_sum
print "Time Taken: " + str(time.time()-start)


sum_check = 0
for i in range(5,size+1):
  sum_check += i
print "Time Taken: " + str(time.time()-start)

