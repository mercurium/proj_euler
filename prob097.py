def rep_sq(n, pow, mod):
  if pow == 1:
    return n % mod
  i = 1
  lst = [1,n]
  while 2 **i <= pow:
    lst = lst + [lst[i]**2 %mod]
    i = i+1 #up till now is just compiling the list of pow
  
  pows = [0]
  power = pow
  while power > 0:
    pows = pows + [power % 2]
    power = power //2 
  
  product = 1
  for i in range(0,len(pows)):
    if pows[i] == 1:
      product = product * lst[i] % mod
  return product
  
print (rep_sq(2,7830457, 10**10) *28433+1 ) %10**10
