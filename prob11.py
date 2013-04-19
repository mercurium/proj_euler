import string
import time
start = time.time()

size = 20

temp = open('prob11lst.txt','r')
lst = string.split(temp.read(),'\n')

for i in range(0, len(lst)):
  lst[i] = string.split(lst[i],' ')

for i in range(0,size):
  for j in range(0,size):
    lst[i][j] = int(lst[i][j])
    
    
max = 0

for i in range(0,size):
  for j in range(0, size-4):
    val = lst[i][j]*lst[i][j+1]*lst[i][j+2]*lst[i][j+3]
    if val > max:
      max = val
print max

for i in range(0,size-4):
  for j in range(0, size):
    val = lst[i][j]*lst[i+1][j]*lst[i+2][j]*lst[i+3][j]
    if val > max:
      max = val
print max

for i in range(0,size-4):
  for j in range(0, size-4):
    val = lst[i][j]*lst[i+1][j+1]*lst[i+2][j+2]*lst[i+3][j+3]
    if val > max:
      max = val
print max


for i in range(4,size):
  for j in range(0, size-4):
    val = lst[i][j]*lst[i-1][j+1]*lst[i-2][j+2]*lst[i-3][j+3]
    if val > max:
      max = val
print max

print "Time Taken: " + str(time.time()-start)
