#NOTE TODO need to solve it
import time
START = time.time()
SIZE = 500

vals = [0,1]+ [2] * (SIZE-1) #Using 2 to indicate that we haven't checked it yet.
for i in range(2,SIZE+1):
    if vals[i] == 2:
        for j in range(i,SIZE+1, i):
            if vals[j] == 2: #first time setting its value
                vals[j] =-1 
            else:
                vals[j] *= -1
        for j in range(i**2,SIZE+1,i**2): #All numbers that are not squarefree are 0
            vals[j] = 0 
#print vals

P = [0] * len(vals)
N = [0] * len(vals)
for i in range(1,SIZE+1):
    P[i] = P[i-1] + (vals[i] == 1)
    N[i] = N[i-1] + (vals[i] == -1)

count = 0
off   = [0] * 100

for a in range(1,SIZE+1):
    b = a
    for b in range(a,SIZE+1):
        Pab = P[b] - P[a-1]
        Nab = N[b] - N[a-1]
        if 99 * Nab <= 100 * Pab and 99 * Pab <= 100 * Nab:
            count +=1 
            off[Nab-Pab] +=1
            print a,b

print off
print count
print "Time Taken:", time.time() - START
