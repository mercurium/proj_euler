import time
start = time.time()

size = 1500

vals = dict()

for m in xrange(2,size):
  if m**2 > 1500000: break
  for n in xrange(1,m):
    val = 2*m*(m+n)

    if val > 1500000: break
    for k in xrange(1,125001):
      valz = k * val
      if valz > 1500000: break
      a,b = m*m*k - n*n*k, 2*m*n*k
      if a > b: a,b = b,a
      try:
        vals[valz].add((a,b))
      except:
        vals[valz] = set()
        vals[valz].add((a,b))
     
count = 0
for i in vals.keys():
  if len(vals[i]) == 1:
    count +=1

print count
  
print "Time Taken: " + str(time.time()-start)

#http://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
#161667
#Time Taken: 9.80598711967 (on laptop)
#Time Taken: 4.45831394196 (on desktop)

