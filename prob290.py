import string
import math


lst = []
for i in range(0,1001):
  lst += [137* i]


for j in range(0,len(lst)):
  sum = 0
  wd = str(lst[j])
  for i in range(0,len(wd)):
    sum += int(wd[i])
  lst[j] = sum

count=0
last = 0
for j in range(0,len(lst)):
  sum = 0
  wd = str(j)
  for i in range(0,len(wd)):
    sum += int(wd[i])
  if sum == lst[j]:
    print j, 137*j, sum
    count = count+1

print count    
