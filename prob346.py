import time
start = time.time()

size = 10**12
values = set([1])

i = 2
power = 2
val = 8
while (val-1)/(i-1) < size:
  bs = size * (i-1)+1
  while val < bs:
    values.add((val-1)/(i-1))
    val *= i
  i+=1
  val = i**3

print sum(values)
print "Time taken:", time.time()-start

"""~/Desktop/python_projects/proj_euler $python prob346.py
336108797689259276
Time taken: 8.93407607079 on laptop
Time taken: 1.16682481766 on desktop
"""
