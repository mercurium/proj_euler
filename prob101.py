from scipy import interpolate
import time
start = time.time()



def val(a,b):
  sumz = 0
  for i in range(len(a)+1):
    sumz += a[i] * b**i
  return sumz

def fn(n):
  return 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10
y = [fn(x) for x in range(1,11)]
sumz = 0
for i in range(1,11):
  sumz += val(interpolate.lagrange(range(1,i+1),y[:i]),i+1)

print int(sumz)
print "Time Taken:", time.time() - start
  

"""
Lol... used the scipy lagrange interpolation method to do all the work
"""
