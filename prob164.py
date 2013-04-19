import time
import copy
start = time.time()
size = 10
leng = 20

#for the beginning, we use first to denote the number of ways to pick a first digit. Obviously # of ways to pick the first digit for each first digit = 1 (besides 0 since we don't have leading zeroes)

#then we can compute the possible second digits. After that, we make an n by n chart keeping track of all endings. Since we only care about the last two digits, we keep a chart of how many numbers end with a certain sequence. We update this the required number of times (20). and get the answer: 378158756814587

first = [0]+ [1]*(size-1) #first digit of list
current = [0]*size  #this is the current row that we care about

for i in range(0,size):
  for j in range(0,size-i):
    current[i] += 1 #this updates current to be the second digit

chart = [[]]*size #row of chart = first digit 
for i in range(0,len(chart)):
  chart[i] = [0]*size #we're making an n by n chart to keep track of the last two digits

chart2 = copy.deepcopy(chart)#col of char = second digit

zeroes = [[0]*size for x in range(0,size)]

for i in range(1,len(chart)):
  for j in range(0,len(chart)):
    if i+j < size:
      chart[i][j] = 1 #this part is computing the n by n table based on the first two digits of the number


for loopss in range(0, leng-2):
  for k in range(0,size):
    for i in range(0,size-k):
      for j in range(0,size-i-k):
        if i+j+k < size:
          chart2[j][k] += chart[i][j] #if i+j+k < size, then we add one to the count of the string ending with jk
  chart = copy.deepcopy(chart2) #make the computed one the current chart
  chart2 = copy.deepcopy(zeroes) #reset the chart to all zeroes


sum = 0 #this is summing up the digits
for i in range(0,size):
  for j in range(0,size):
    sum+= chart[i][j]

print sum
print "Time Taken: " + str(time.time()-start)
