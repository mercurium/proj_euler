import time
start = time.time()

def val_calc(q):
  lst = [1] + [ (1-x/q) for x in xrange(1,51)]
  p = [1]+[0]*50
  new_p = [0]*51
  for i in xrange(1,51):
    new_p[0] = p[0] * (1.-lst[i])
    for j in xrange(1,51):
      new_p[j] = p[j]*(1.-lst[i])+p[j-1]*lst[i]
    p = new_p[:]
  return p[20]

print val_calc(50.)
print "Time Taken: ", time.time() - start

sumz = 50.
val = val_calc(50.)
digz = -1
for i in xrange(0,11):
  for dig in xrange(0,10):
    num = sumz + dig/10.**i
    if val_calc(num) < .02:
      break
    if val_calc(num) < val:
      val = val_calc(num)
      digz = dig
  sumz += digz/10.**i
  print sumz

print sumz
print "Time Taken: ", time.time() - start
"""
>>> val_calc(52.64945719530)
0.020000000000052105

Congratulations, the answer you gave to problem 286 is correct.

You are the 973rd person to have solved this problem.


So I was too lazy to write a program to compute it so I just did it by hand lololol.
"""
