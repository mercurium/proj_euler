import string
import math
import time
start = time.time()



def reverse(num):
  return str(num)[::-1]
  
sum = 0

for i in range(1,10): #numbers from 0-9
  if reverse(bin(i)[2:]) == bin(i)[2:]:
    print i, bin(i)
    sum = sum + i
for i in range(1,1000): #numbers with an even # of digits
  num = int(str(i) + reverse(i))
  if reverse(bin(num)[2:]) == bin(num)[2:]:
    print num, bin(num), i
    sum = sum + num

for i in range(1,100):
  for j in range(0,10):
    num = int(reverse(i) +str(j)+ str(i))
    if reverse(bin(num)[2:]) == bin(num)[2:]:
      print num, bin(num)
      sum = sum + num
print sum

print "Time Taken: " + str(time.time()-start)
