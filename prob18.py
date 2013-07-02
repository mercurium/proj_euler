import string
import time
start = time.time()
#the efficiency for this code comes from the fact that I only need to compute a value for (row,col) once and then it's stored away for future use. An analogy would be F(n) = nth fibonacci number and finding:
#F(n) = F(n-1)+F(n-2) = F(n-2)+F(n-3)+F(n-3)+F(n-4)  = ...
#as opposed to finding F(1) to F(n-1) once then using that for finding F(n)

temp = open('prob18lst.txt','r')
lst = string.split(temp.read(), '\n')

for i in xrange(0, len(lst)):
  lst[i] = string.split(lst[i],' ')

lst = lst[:-1] 

for i in xrange(0, len(lst)):
  for j in xrange(0, len(lst[i])):
    lst[i][j] = int(lst[i][j])
ans = lst[:] #up to here is just cleaning up the input

#this computes the max value for getting to each spot (row,col) and then stores it for future use
for i in xrange(1,len(lst)): 
  for j in xrange(0, len(lst[i])):
    if j == 0:
      lst[i][j] += lst[i-1][0]
    elif j == len(lst[i]) -1:
      lst[i][j] += lst[i-1][j-1]
    else:
      lst[i][j] += max(lst[i-1][j], lst[i-1][j-1])

print max(lst[len(lst)-1])

print "Time Taken: " + str(time.time()-start)
