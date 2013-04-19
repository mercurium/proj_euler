import time
import copy
start = time.time()


#(0,0) = PP, (0,1) = PA, (1,0) = AP, (1,1) = AA
c = [[1,1],[1,1]] 
c2 =[[0,0],[0,0]]

lst = [1,2,4] + [0]*28
for i in range(3,31):
  c2[0][0] = c[0][0]+c[1][0] #PPP or APP
  c2[0][1] = c[0][0]+c[1][0] #PPA or APA
  c2[1][0] = c[1][1]+c[0][1] #AAP or PAP
  c2[1][1] = c[0][1] #AAP
  c = copy.deepcopy(c2)
  lst[i] = c[0][0]+c[0][1]+c[1][0]+c[1][1]
print lst[:5]

sum = 0
for i in range(0,30):
  sum += lst[i] *lst[30-i-1]

sum+= lst[-1]
print sum

print "Time Taken: " + str(time.time()-start)
