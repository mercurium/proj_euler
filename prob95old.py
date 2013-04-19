import time
start = time.time()

size = 30000
lst = [0]*size

for i in range(1,size):
  for j in range(2*i,size,i):
    lst[j] += i #up to here we're marking what the sum of divisors is.


results = [0]*size
results[0] = -1
results[1] = -1
#we're going to iterate one at a time through the list to find out which ones of them are loops. Since we don't know how long we need to go till we hit a loop, we'll keep going until we hit a number we've recorded the result of.

for i in range(1,size):
  if lst[i] > size: #if it goes past 1 million, we ignore it
    results[i] = -100
  if results[i] ==0:#if we haven't touched it yet
    current = lst[i]#grab the next element
    prev = i
    results[i] = -1 #put it as -1 for now
    while current < size and current != i and results[current] == 0:#we'll keep decrementing till we see a loop
      results[current] = results[prev] -1
      prev = current
      current = lst[current]
    if current >= size:
      #print "too big", current, i #if we exceed 1 million, we keep all num neg.
      pass
      #however, when we break out of the loop, we want to change the stuff we did to it.
    elif current ==i:
      val = results[i]-results[prev]+1
      current = lst[i]
      while current != i:
        results[current] = val
        current = lst[current]
      results[current] = val
      
      ##################################################33
    elif lst[current] < lst[prev]: #this is the chunk of code that needs fixing
      val = 1
      marker = current
      current =lst[current]
      while current != marker:
        results[current] = val
        current = lst[current]
      
        
      
for i in range(1,size):
  if results[i] > 0:
    print i, results[i]
#print lst[220],lst[284]
#print results[220],results[284]
print lst[12496],lst[lst[12496]],lst[lst[lst[12496]]],lst[lst[lst[lst[12496]]]],lst[lst[lst[lst[lst[12496]]]]]
print results[12496],results[14288],results[15472],results[14536],results[14264]






print "time taken: " +str(time.time()-start)
    
    
