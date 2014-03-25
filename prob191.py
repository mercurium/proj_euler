import time, copy
START = time.time()

#(0,0) = PP, (0,1) = PA, (1,0) = AP, (1,1) = AA
c = [[1,1],[1,1]] 
c2 =[[0,0],[0,0]]

lst = [1,2,4] + [0]*28
for i in xrange(3,31):
    c2[0][0] = c[0][0]+c[1][0] #PPP or APP
    c2[0][1] = c[0][0]+c[1][0] #PPA or APA
    c2[1][0] = c[1][1]+c[0][1] #AAP or PAP
    c2[1][1] = c[0][1] #AAP
    c = copy.deepcopy(c2)
    lst[i] = c[0][0]+c[0][1]+c[1][0]+c[1][1]
print lst[:5]

sumz = 0
for i in xrange(0,30):
    sumz += lst[i] *lst[30-i-1]

sumz+= lst[-1]
print sumz

print "Time Taken:", time.time() - START
