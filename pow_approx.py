import math

#This method will return at least 'dig' of the first digits.
def approx_pow(n,powz,dig):
  if powz == 0: return 1
  if powz == 1: return truncate(n,dig)

  val = int(math.log(powz,2))
  lst = [1,n] + [0] * val
  for i in xrange(2,len(lst)):
    lst[i] = truncate(lst[i-1]**2,dig)

  pows = [0] * (val+1)
  power = powz
  for i in xrange(0,len(pows)):
    pows[i] = power % 2
    power = power //2
  product = 1
  for i in xrange(0,len(pows)):
    if pows[i] == 1:
      product = truncate(product * lst[i+1],dig)
  return product

def truncate(num, dig):
  num_len = len(str(num))
  if num_len < dig:
    return num
  return num/10**(num_len -dig)
