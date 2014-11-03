"""
These are the random equations / throwaway code I wrote to solve this problem. I'm reluctant to throw it away, so I'm storing it here.

#  num   = (y * (pow(y, SIZE, MOD) - 1) * ext_gcd(y-1,MOD)[0]) % MOD


#Yeah, these two functions are hardcoded for the sake of this problem. Being specific does help speed up the solution, so no regrets :P
def cubicEqn(k, x):
  return k**3 -x + (k*x)**2 - k*x**3

def derive(func, pt):
    step = .000001
    return (func(pt+step)-func(pt))/step

def newtons(start, func, error):
  nextX = start - func(start)/derive(func,start)
  count = 0
  while abs(func(nextX)) > error:
    #print count, '\t', nextX
    start = nextX
    nextX = start - func(start)/derive(func,start)
    count +=1
  return nextX

for k in xrange(1,10):
  func = lambda x: cubicEqn(k,x)
  a    = newtons(0,func,.0000001)
  b    = (k - a) /2
  c    = math.sqrt(k**2/a - b**2)
  checks = [k**2 - a*(b**2+c**2), 1./k - 2*a*b -b**2 - c**2]
  answer = ( (a + b)**2 + c**2) * (-2*b)

  print k, answer, [round(x,4) for x in checks]



1/x = (k/x)^2(k+x^2) - kx
x   = k^2(k+x^2) - kx^3
0   = k^3 - x + k^2x^2 - kx^3

solutions will be
(x-a), (x-b-cj), (x-b+cj)

And this means that the formula comes out to:
2b( (a+b)^2 + c^2 )

==================
k   = 2b+a
1/k = 2ab + b^2 + c^2
k^2 = ab^2 + ac^2
==================

Well, this is both yay and meh at the same time...

The answer, naively is...

for i in range(1,10^6+1):
  for x in range(1,10^6+1):
    (x^2-1)^i:1

sumz = 0
for i in range(1,SIZE+1):
  for x in range(1,SIZE+1):
    sumz += (x**2-1)**i
print sumz


"""
