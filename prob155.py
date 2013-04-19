import time
start = time.time()

def gcd(a,b):
  if a==0: return b
  return gcd(b%a,a)

def combine(a,b):
  x = a[0]*b[1] + a[1]*b[0]
  y = a[1]*b[1]
  return (x/gcd(x,y),y/gcd(x,y))


A = [[(0,0)],[(1,1)]]
A_set = set([(1,1)])
A[1] = [(1,1)]
count = 1

for n in range(2,19):
  cap_lst = []
  for i in range(1,n):
    j = n-i
    
    for a in A[i]:
      for b in A[j]:
        item = combine(a,b)
        if item not in A_set:
          A_set.add(item) #C1
          A_set.add((item[1],item[0]))
          cap_lst.append(item) #C1
          cap_lst.append((item[1],item[0]))
          
  A.append(cap_lst)
  count+= len(cap_lst)
  print count, n
  print "Time Taken:", time.time() -start
  
print count
print "Time Taken:", time.time() - start    

"""
3857447 18
Time Taken: 46.6547019482

So I realized later on that if we have a number of circuits with n-1 transistors, we can easily construct a new value if we just put that in parallel with a nth new transistor.

In addition, we can parallelize shit from like A(i) and A(n-i) to get a new value (most of the time?).

(C1) Also, if a/b is a valid circuit value, then so is b/a.

(C2) I used combine(a,b) to store the values as tuples to make sure I had precision and no floating point errors.

"""

