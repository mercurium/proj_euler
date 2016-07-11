"""
Sighh.... need to fix this later T.T

"""


#from m_rTest import m_r


temp_lst = [0]*10**5
primes_set = set([])
for i in range(2,len(temp_lst)):
  if temp_lst[i] == 0:
    primes_set.add(i)
    for j in range(2*i,len(temp_lst),i):
      temp_lst[j] +=1



def gcd(a,b):
  if a == 0: return b
  return gcd(b%a,a)



def pollard_rho(n):
  #if m_r(n): return [n]

  def func(x):
    return (x**2+1)%n

  def func2(x):
    return (x**2+3)%n


  x,y = 2,2
  d = 1
  while d==1:
    x = func(x)
    y = func(func(y))
    d = gcd(abs(x-y),n)


  if d==n:
    d=1
    while d==1:
      x = func2(x)
      y = func2(func2(y))
      d = gcd(abs(x-y),n)
  return d
  #if m_r(d): return sorted([d]+pollard_rho(n/d))
  #return sorted([pollard_rho(n/d)]+[pollard_rho(d)])

p_r = pollard_rho

for i in range(2,10**3):
  a = i
  while a%2 ==0: a/=2
  if a!= 1 and p_r(a) == i and i not in primes_set:
    print i

print p_r(1231314242221111)
print p_r(3494675165431)
print p_r(16514878883212313151)
