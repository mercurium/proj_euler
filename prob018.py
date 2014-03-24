import string
import time
START = time.time()
#the efficiency for this code comes from the fact that I only need to compute a value for (row,col) once and then it's stored away for future use. An analogy would be F(n) = nth fibonacci number and finding:
#F(n) = F(n-1)+F(n-2) = F(n-2)+F(n-3)+F(n-3)+F(n-4)	= ...
#as opposed to finding F(1) to F(n-1) once then using that for finding F(n)

temp = open('prob18inputz.txt','r')
inputz = string.split(temp.read(), '\n')

for i in xrange(0, len(inputz)):
	inputz[i] = string.split(inputz[i],' ')

inputz = inputz[:-1] 

for i in xrange(0, len(inputz)):
	for j in xrange(0, len(inputz[i])):
		inputz[i][j] = int(inputz[i][j])
ans = inputz[:] #up to here is just cleaning up the input

#this computes the max value for getting to each spot (row,col) and then stores it for future use
for i in xrange(1,len(inputz)): 
	for j in xrange(0, len(inputz[i])):
		if j == 0: #end of rows --> only need to look at one.
			inputz[i][j] += inputz[i-1][0]
		elif j == len(inputz[i]) -1:
			inputz[i][j] += inputz[i-1][j-1]
		else:
			inputz[i][j] += max(inputz[i-1][j], inputz[i-1][j-1])

print max(inputz[len(inputz)-1])

print "Time Taken:", time.time() - START
