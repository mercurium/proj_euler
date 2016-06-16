import time
START = time.time()
start = 101010103
end = 138935382

done = False
for i in xrange(start,end,10):
  if str(i**2)[::2] == '123456789':
   print i
   done = True
   break
if not done:
    for i in xrange(start+4,end,10):
      if str(i**2)[::2] == '123456789':
       print i
       break
print "Time Taken:", time.time() - START

"""
08:42 ~/Desktop/python_projects/proj_euler $ python prob206.py
138901917
Time Taken: 3.06542801857

"""
