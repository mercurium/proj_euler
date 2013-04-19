import string
import math
import time
from itertools import permutations
start = time.time()

def update(type,prev):
  newset = set()
  for i in range(20,150):
    n = valzer(type,i)
    if len(str(n)) == 4 and n/100 in prev:
      newset.add(n%100)
  return newset

def update_rev(type,nextz):
  newset = set()
  for i in range(20,150):
    n = valzer(type,i)
    if len(str(n)) == 4 and n%100 in nextz:
      newset.add(n/100)
  return newset


def valzer(type,i):
  if type == 3: return i*(i+1)/2
  elif type==4: return i**2
  elif type ==5: return i*(3*i-1)/2
  elif type ==6: return i*(2*i-1)
  elif type ==7: return i*(5*i-3)/2
  else: return i*(3*i-2)

tri = set()


for i in range(40,150):
  n = i*(i+1)/2
  if len(str(n)) == 4:
    tri.add(n%100)

itemzz = permutations([[set(),4],[set(),5],[set(),6],[set(),7],[set(),8]])
answer = []
for item in itemzz:
  item = ([tri,3],) + item
  item[0][0] = update(3,range(0,100))
  
  for dammitdonttakesolong in range(0,10):
    for i in range(1,len(item)):
      item[i][0] = update(item[i][1],item[i-1][0])
    item[0][0] = update(item[0][1],item[-1][0])
    
    answer = item
      
  
  if len(item[0][0]) == 1 and len(item[1][0]) == 1 and len(item[2][0]) == 1 :
    break
  else:
    print "darn, those were not the tuples we were looking for."

print answer
print "WE FOUND THEM :D YAY DADDY!"



print "Time Taken: " + str(time.time()-start)








