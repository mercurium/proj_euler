#NOTE TODO need to solve it
import time
START = time.time()
SIZE = 20 

vals = [0,1,1,3] + [0]*(SIZE-3)
for i in range(4,SIZE+1):
    if i%2 == 0:
        vals[i] = vals[i/2]
    if (i-1)%4 == 0:
        k = (i-1)/4
        vals[i] = 2*vals[2*k+1] - vals[k]
    if (i-3)%4 == 0:
        k = (i-3)/4
        vals[i] = 3*vals[2*k+1] - 2*vals[k]

print sum(vals), vals
