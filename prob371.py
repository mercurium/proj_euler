import time
start = time.time()

#keys will be of the form (vals that we can find to win)
vals = dict() 
vals[500] = 0
valz = dict()
valz[499] = 1
#vals[v] = (v + (1000-2*v-1)* vals[v+1] + vals[v] * (v+1))/1000.
#vals[v] = (v +vals[v+1]*v) /(999- v)
def calc(v):
  if v in vals: return vals[v]
  vals[v] = ((998.-2*v)* calc(v+1)+calc500(v)+1000.)  / (999.-v)
  return vals[v]
def calc500(v):
  if v in valz: return valz[v]
  valz[v] = ((998-2*v)* calc500(v+1) +1000.)  / (999.-v)
  return valz[v]  

print calc(0)

print "Time Taken:", time.time() - start
"""~/Desktop/python_projects/proj_euler $python prob371.py
40.6636809666
Time Taken: 0.00161194801331
"""
