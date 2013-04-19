from primes import *
import time
start = time.time()

def remove_dupl(lst):
  return list(set(lst))

lst = [0] * 150000
for i in range(2,len(lst)):
  if lst[i] == 0:
    for n in range(i*2,len(lst),i):
      lst[n]+=1
  
print "time elapsed = " + str(time.time()-start)

for i in range(0,len(lst)-4):
  if lst[i] == 4 and lst[i+1]==4 and lst[i+2]==4 and lst[i+3]==4:
    print i
    break
print "time elapsed = " + str(time.time()-start)
