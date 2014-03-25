#NOTE TODO need to solve it
import time
start = time.time()

setz = set()

for n in xrange(1,2001):
  for m in xrange(n+1,n+2000//n+1):
    if n*(m-n) > 2000: break
    if n%2==0 or (m-n)%2 == 0:
      a,b,c = m**2-n**2, 2*m*n, m**2 + n**2
      print (a*b/2.)/(a+b+c)
      if a > b: a,b = b,a
      setz.add((a,b,c))

sumz = sum([(s[0]+s[1]+s[2]) for s in setz])
print sumz, len(setz)
print "Time Taken:", time.time() - start



#perimeter = (m^2-n^2) +2mn + (m^2+n^2) = 2m^2 + 2mn = 2m(m+n)
#area = (m^2-n^2)*2mn/2 = mn(m-n)(m+n)
#so the ratio is n(m-n)/2:1...


#LOL OOPS. I forgot about when the triangle isn't a right triangle :D;;;
