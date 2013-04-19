from primes import *
from math import sqrt
import math
import time
start = time.time()

#the way to get the next item in the list is such:
# A' = a*B -A
# B' = (d-A'*A')/B
# a' = int((sqrt(d)+A')/B')
def transform(A,B,a,d):
  A = a*B-A
  B = (d-A*A)/B
  a = int((sqrt(d)+A)/B)
  return A,B,a

count = 0
for d in range(2,10000): #iterate from 2 to 10000
  if int(sqrt(d+.2))**2 != d:
    grub =transform(0,1,int(sqrt(d)),d)
    lst_A =[grub[0]]
    lst_B =[grub[1]]
    lst_a =[grub[2]] #this updates the list
    
    grub =transform(lst_A[0],lst_B[0],lst_a[0],d)
    lst_A += [grub[0]]
    lst_B += [grub[1]]
    lst_a += [grub[2]] #this updates the list again
    i=1
    while lst_A[-1]!=lst_A[0] or lst_B[-1]!=lst_B[0] or lst_a[-1] != lst_a[0]: #while it hasn't repeated yet...
      grub =transform(lst_A[i],lst_B[i],lst_a[i],d)
      lst_A += [grub[0]]
      lst_B += [grub[1]]
      lst_a += [grub[2]]
      i+=1 #our fancy loop counter


    if len(lst_a)%2 == 0: #if it has an odd cycle, add to count
      count += 1
print count


print "Time taken: " + str(time.time()-start)


