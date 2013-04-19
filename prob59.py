import string
import time

start = time.time()
temp = open('prob59lst.txt','r')
lst = string.split(temp.read(),',')


counter = {}
for i in range(0, len(lst)):
  lst[i] = int(lst[i]) #int-ifying all the entries

sum = 0
for i in range(0,len(lst)):
  if i % 3 == 0:
    lst[i] = lst[i]^103
  if i % 3 == 1:
    lst[i] = lst[i]^111
  if i % 3 == 2:
    lst[i] = lst[i]^100
  sum = sum + lst[i]

for i in range(0,len(lst)):
  lst[i] = chr(lst[i])

print string.join(lst,'')
print sum

print "Time Taken:", time.time()-start
