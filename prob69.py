import sys

def factor_rec(val, count):
  while(val >= count):
    if val % count == 0:
       return count
    count = count + 1


def factor(val):
  if val == 1:
    return [1]
  temp = factor_rec(val, 2)
  return [temp] + factor(val/temp)
  
def totient(n):
  lst = factor(n)[:-1]
  print lst
  result = 1.0
  for i in range(0,len(lst)):
    if i==0 or lst[i] != lst[i-1]:
      result = result * (lst[i]-1)
    else:
      result = result * lst[i]
  return result


