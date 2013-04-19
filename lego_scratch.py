def test(n): #this is the case of size 1 and 2 blocks. Fibo
  sumz = 0
  for a in range(0,n//2+1):
    sumz += fact(n-a) /(fact(a) * fact(n-2*a))
  return sumz
  
def test2(n):
  sumz = 0
  for a in range(0,n//3+1):
    for b in range(0, (n-3*a)//2+1):
      m = n - b -2*a
      sumz +=fa(m)/(fa(a)*fa(b)*fa(n-2*b-3*a))
  return sumz
