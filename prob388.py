import time
START  = time.time()
SIZE   = 10**6

divArr = [0]*(SIZE+1)

for i in xrange(2, SIZE + 1):
  if divArr[i] == -1: #number isn't squarefree, we don't want it.
    continue

  if divArr[i] == 0:
    for j in xrange(i,SIZE,i):
      #ignore the number if it isn't squarefree.
      if divArr[j] != -1:
        divArr[j] += 1
    for j in xrange(i**2, SIZE, i):
      divArr[j] = -1

count = SIZE**3 - 1
for i in xrange(2, SIZE/2 + 1):
  if divArr[i] == -1 or i * 2 > SIZE:
    # skip cases where i contains a square
    continue

  a = (SIZE/i) ** 3 - 1

  if divArr[i] % 2 == 1:
    count -= a

  else:
    count += a


print count, count - 831909254469114121
print "Time Taken:", time.time() - START
