import time
start = time.time()

grabbag = {1:0}
max = 0
max_key = 0

def grab(i):
  if grabbag.get(i,-1) == -1:
    if i % 2 == 0:
      temp = 1 + grab(i/2)
    else:
      temp = 1 + grab(3 * i + 1)
    grabbag[i] = temp
  return grabbag[i]

for i in range(2,10**6):
  if grab(i) > max:
    max = grab(i)
    max_key = i
    
    
print max, max_key

print "Time Taken: " + str(time.time()-start)
