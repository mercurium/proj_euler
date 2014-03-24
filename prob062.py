import time
import string
start = time.time()

d = {}

key = ''
for i in range(0,10000):
  m = string.join(sorted(str(i**3) ),'' )
  try: d[m] += [i]
  except: d[m] = [i]
  if len(d[m]) == 5:
    print min(d[m])**3, min(d[m])
    break
print "Time Taken: " + str(time.time() -start)
