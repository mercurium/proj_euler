import time
start = time.time()

mod = 14**8

vals = {}

def A(m,n):
  if (m,n) in vals: return vals[(m,n)]
  if m == 0: 
    vals[(m,n)]= n+1
  elif m > 0 and n == 0: 
    vals[(m,n)] = A(m-1,1)
  elif m > 0 and n > 0:
    vals[(m,n)] = A(m-1,A(m,n-1))
  return vals[(m,n)]
  
print A(2,2)
print "Time Taken:", time.time() -start
