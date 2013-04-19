import time
start = time.time()

count = 0
perfect_count = 0
for i in xrange(1,5):
  print i
  for j in xrange(1,i):
    if (i**2+j**2)**2 > 10**16:
      break
    m = i**2-j**2
    n = 2*i*j
    m,n = max(m,n),min(m,n)
    a = m**2-n**2
    b = 2*m*n
    c = m**2+n**2
    
    count+=1
    if (a*b)%168==0:
      perfect_count +=1

print count-perfect_count

print "Time Taken:", time.time()-start


"""
...Huh... a question where the answer is 0 o.O

a = m^2-n^2
b = 2mn
c = m^2+n^2
m = i^2-j^2
n = 2ij

a = i^4 - 6i^2j^2 + j^4
b = 2i^3j - 2ij^3
c = i^4 + 2i^2j^2 + j^4 = (i^2+j^2)^2

Oh... fail. Duhh...
a^2+b^2 = c^2
mod 2, we have 0+1=1 (since no primitive)
mod 3: 0+1 = 1 (since no primitive)
mod 4: 0+1 = 1
mod 7: 0+1 = 1 (only squares are 0,1,2,4)
...don't feel like mathing it out.

ab = ij(i^4-6i^2j^2+j^4)(i-j)(i+j)



"""
