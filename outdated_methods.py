#Most of the methods in here are out of date, since I wasn't as familiar with python and was implementing methods that already exist. However, some of these are of use to me if I modify them so I'm keeping them

def mergesort(lst):
  if len(lst) == 1:
    return lst
  elif len(lst) == 2:
    if lst[0] < lst[1]:
      return lst
    return [lst[1],lst[0]]
  else:
   lst1 =mergesort(lst[0:len(lst)/2])
   lst2 =mergesort(lst[len(lst)/2:])
   ans = []
   while len(lst1) != 0 and len(lst2) != 0:
     if lst1[0] < lst2[0]:
       ans = ans + [lst1[0]]
       del lst1[0]
     else:
       ans = ans + [lst2[0]]
       del lst2[0]
   ans = ans + lst1+lst2
   return ans

def reverse(num):
  s = str(num)
  result = ''
  for i in range(0,len(s)):
    result = s[i] + result
  return int(result)


def rep_sq(n, powz, mod):
  if powz == 0: return 1
  if powz == 1: return n % mod


  val = int(math.log(powz,2))
  lst = [1,n] + [0] * val
  for i in range(2,len(lst)):
    lst[i] = lst[i-1]**2 % mod

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
