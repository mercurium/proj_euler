import math

def rep_sq(n, powz, mod):
  if powz == 0: return 1
  if powz == 1: return n % mod
  
  
  val = int(math.log(powz,2))
  lst = [1,n] + [0] * val
  for i in range(2,len(lst)):
    lst[i] = round(lst[i-1]**2 % mod,4)
  
  pows = [0] * (val+1)
  power = powz
  for i in range(0,len(pows)):
    pows[i] = power % 2
    power = power //2 
  product = 1
  for i in range(0,len(pows)):
    if pows[i] == 1:
      product = product * lst[i+1] % mod
  return product
  
  
rep_sq(2.1,100000,10**8)
