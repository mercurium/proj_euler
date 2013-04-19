import string
import time
start = time.time()



def reverse(num):
  return int(str(num)[::-1])


count = 0
for i in range(1,10000):
  lychrel = 1
  n = i
  for j in range(1,51):
    n = n+reverse(n)
    if n == reverse(n):
      lychrel = 0

      break
  if lychrel == 1:
    count = count+1

print count
print "Time Taken: " + str(time.time()-start)
