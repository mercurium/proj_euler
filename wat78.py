import time
start = time.time()



target = 5000

def addp (value, tab):
  for (j, e) in tab.items():
    for i in xrange (value,1+target-j,value):
      t = i + j
      try: tab[t] = e+tab[t]
      except KeyError: tab[t] = 1

tab = {0: 1}
for i in range (1, target+1): 
  addp (i, tab)
  #print tab[i]
  if tab[i]%10**6 ==0:
    print i
    break
#print tab[target]

print "Time Taken: " + str(time.time()-start)
