import string
true = True
false = False

def mergesort(lst):
  if len(lst) == 1: return lst
  elif len(lst) == 2:
    if lst[0] < lst[1]: return lst
    return lst[1] +lst[0]
  else:
   lst1 =mergesort(lst[0:len(lst)/2])
   lst2 =mergesort(lst[len(lst)/2:])
   ans = ''
   while len(lst1) != 0 and len(lst2) != 0:
     if lst1[0] < lst2[0]:
       ans = ans + lst1[0]
       lst1 = lst1[1:]
     else:
       ans = ans + lst2[0]
       lst2 = lst2[1:]
   ans = ans + lst1+lst2
   return ans


def rot(a,b):
  a = mergesort(str(a))
  b = mergesort(str(b))
  if a ==b:
    return True
  return False


for i in range(100000,300000):
  if rot(i,2*i) and rot(i,3*i) and rot(i,4*i) and rot(i,5*i) and rot(i,6*i):
    print i, 2*i, 3*i,4*i,5*i,6*i
    break
