import string
from math import log

temp = open('base_exp.txt','r')
lst = string.split(temp.read(),'\n')[:-1]
for i in xrange(0,len(lst)):
  lst[i] = string.split(lst[i],',')
  lst[i][0] = int(lst[i][0])
  lst[i][1] = int(lst[i][1])

maxz = 0
index = 0
for i in xrange(0,len(lst)):
  if maxz < log(lst[i][0],10) * lst[i][1]:
    maxz = log(lst[i][0],10) * lst[i][1]
    index = i+1

print index, maxz

