
def peller(lst): #returns h,k where we have h/k --> n
  if len(lst) == 1:
    return lst[0],1
  a = 1
  b = lst[-1]
  for j in xrange(len(lst)-2,0,-1):
    b_n = lst[j]*b+a
    a = b
    b = b_n
  a = a + lst[0]*b
  return a, b #this function adds up a_1+1/(a_2+1/(a3+...))


def convergents(lst, n):
#this function finds the successive convergents of the list until h^2 - n *k^2 = 1
  for i in xrange(1,len(lst)+1):
    a,b = peller(lst[0:i])
    if a**2 - b**2 * n == 1:
      #print a, b, n, 'abbaa!'
      return a,b
  print 'ragequit your fault...'
  return -1,-1
