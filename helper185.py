import time, string
START  = time.time()
SIZE   = 16
NUMDIG = 10

dataFile = open('data185.txt','r')
data     = dataFile.read()
data     = filter(len, data.split('\n'))

data     = [string.split(line)[0] for line in data]

for index in xrange(16):
  s = string.join(sorted(([line[index] for line in data])), '')
  maxOccur = max([s.count(str(n)) for n in xrange(0,10)])
  print index, maxOccur, s


print "Time Taken:", time.time()-START
