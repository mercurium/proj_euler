import time
import math
start = time.time()


def twoer(n):
  if n == 0:  return 0
  sum = 0
  for i in range(1,int(math.log(n,2)+1)):
    sum += n/2**i
  return sum
def fiver(n):
  if n == 0:  return 0
  sum = 0
  for i in range(1,int(math.log(n,5)+1)):
    sum += n/5**i
  return sum

lst_f = [fiver(x) for x in range(0,2*10**5+1)]
lst_t = [twoer(x) for x in range(0,2*10**5+1)]
#lst_f and lst_t for lists of fives and twos.

count = 0
for n in range(2,101): 
  for j in range(0,n+1):
    f = lst_f[n] - lst_f[j]-lst_f[n-j] #f for five
    t = lst_t[n] - lst_t[j]-lst_t[n-j] #t for two
    if f >= 1 and t >=1:
      count += 1
      print n,j
print count

print "time elapsed = " + str(time.time()-start)














