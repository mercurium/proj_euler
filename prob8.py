import string
import time
start = time.time()
temp = open('prob8input.txt','r')

l = temp.read()

max = 0
total = len(l)

for i in range(0, total - 5):
  val = int(l[i]) * int(l[i+1]) * int(l[i+2]) * int(l[i+3]) * int(l[i+4])
  if max < val:
    max = val
    
print max
print "Time Taken: " + str(time.time()-start)
