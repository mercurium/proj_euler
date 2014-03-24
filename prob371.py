import time
start = time.time()

#keys will be of the form (vals that we can find to win)
vals = dict() 
vals[500] = 0
valz = dict()
valz[499] = 1
def calc(v):
    if v in vals: return vals[v]
    vals[v] = ( (998.-2*v) * calc(v+1) + calc500(v) + 1000.) / ( 999.-v )
    return vals[v]
def calc500(v): #You've seen the 500 plate
    if v in valz: return valz[v]
    valz[v] = ( (998-2*v) * calc500(v+1) + 1000. ) / (999.-v)
    return valz[v]    

print calc(0)
print "Time Taken:", time.time() - start


"""~/Desktop/python_projects/proj_euler $python prob371.py
40.6636809666
Time Taken: 0.00161194801331

So for this problem. At each step, you can either see a plate you've already seen, or a new one that adds to your possible answers, or the 500 one which combines with itself. (Similar to 323... kinda) 

approximate time of solve was dec 2012-jan 2013. I know I was in taiwan when I did it though...
vals[v] = (v + (1000-2*v-1)* vals[v+1] + vals[v] * (v+1))/1000.
vals[v] = (v +vals[v+1]*v) /(999- v)
"""
