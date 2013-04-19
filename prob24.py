import time
start = time.time()

from math import factorial
val = 1000000
fa = factorial

count = [0] * 9
pos = 0
while val > 0:

  while val >= fa(9-pos):
    val = val - fa(9-pos)
    count[pos] = count[pos]+1
  pos = pos +1
  print count
  
print count

items = range(0,10)
answer = [0]*10
for i in range(0,9):
  answer[i] = items[count[i]]
  del items[count[i]]
  print items, answer
  
print answer

print "Time Taken: " + str(time.time()-start)
