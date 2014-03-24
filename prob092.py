import string
import time
start = time.time()


lst = [0]*(10**7+1)
lst[0] = -1
lst[1] = 1
lst[89] = 89

def sq_dig(n):
  item = str(n)
  sum = 0
  for i in range(0,len(item)):
    sum += int(item[i])**2
  return sum

def update(n):
  if lst[n] == 0:
    lst[n] = update(sq_dig(n))
  return lst[n]

for i in range(1,10**7):
  update(i)
  if i == 10**4:
    print "time taken: " + str(time.time()-start)
  if i == 10**5:
    print "time taken: " + str(time.time()-start)
  if i == 10**6:
    print "time taken: " + str(time.time()-start)
print "time taken: " + str(time.time()-start)
start = time.time()

count = 0
for i in range(0,len(lst)):
  if lst[i] == 89:
    count+= 1

print "time taken: " + str(time.time()-start)
print count

#...got the right answer, but it took 75 seconds... murr...

