import string
import time
start = time.time()
true = True
false = False

temp = open('prob49lst.txt', 'r')
lst = string.split(temp.read(),', ')
for i in range(0,len(lst)):
  lst[i] = int(lst[i])

def rotation(a,b,c):
  a,b,c = sorted(str(a)),sorted(str(b)),sorted(str(c))
  return a == b and a == c

def dig(a):
  return string.join(sorted(str(a)),'')    

d = {}
for item in lst:
  if dig(item) in d:
    d[dig(item)] += [item]
  else: d[dig(item)] = [item]
  
lst = d.keys()

for item in lst:
  if len(d[item]) >= 3:
      items = d[item]
      items.sort()
      for i in range(0,len(items)-1):
        for j in range(i+1,len(items)):
          if 2*items[j]-items[i] in items:
            print items[i], items[j], 2*items[j]-items[i]
print "Time Taken:" + str(time.time()-start)
      
      




