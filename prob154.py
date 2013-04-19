import time
import math
start = time.time()



def fiver(n):
  if n == 0: return 1
  return sum([ n/x for x in xrange(1,int(math.log(n,5)+1) ) ])

def twoer(n):
  if n == 0: return 1
  return sum([ n/x for x in xrange(1,int(math.log(n,2)+1) ) ])

size = 2*10**5 # =200000
fivepow = fiver(size) -12
twopow = twoer(size) -12

twos = [0] * (size+1)
fives = [0] * (size+1)
for i in range(2,size+1):
  twos[i] = twoer(i)
  fives[i] = fiver(i)

print "time elapsed = " + str(time.time()-start)

count = 0
eqcount = 0
for x in range(0,size+1):
  for y in range(0,x+1):
    if x + y > size: break
    z = size - x - y
    if fives[x] + fives[y] + fives[z] <= fivepow and twos[x] + twos[y] + twos[z] <= twopow:
      count += 1
      if x == y:
        eqcount +=1
    
print count, eqcount
print count * 2 + eqcount
print "time elapsed = " + str(time.time()-start)














