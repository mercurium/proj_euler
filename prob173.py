#import string
import math

n = 10**6

#for i in range(3,n/4+2):
 # for j in range(1,i):
  #  if i**2-j**2 <= n and (i -j)%2 == 0 :
   #   count = count +1
    #  print i,j, (i**2-j**2)/4

#print count


count = 0
i = 2
while (n - i**2)/(2*i) > 0:
  count = count + (n - i**2)/(2*i)
  print (n - i**2)/(2*i)
  i = i +2


print count
