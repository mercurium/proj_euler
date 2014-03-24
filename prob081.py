import string
import time
temp = open('matrix.txt','r')
lst = string.split(temp.read(),'\n')
start = time.time()
def min(a,b):
  if a > b:
    return b
  return a

for i in range(0,len(lst)):
  lst[i] = string.split(lst[i],',')

lst = lst[:-1] +lst[-1][:-1]
for i in range(0,len(lst)):
  for j in range(0, len(lst[i])):
    lst[i][j] = int(lst[i][j])

for i in range(0,len(lst)):
  for j in range(0, len(lst[i])):
    if i == 0:
      if j != 0:
        lst[i][j] = lst[i][j] + lst[i][j-1]
    else:
      if j == 0:
        lst[i][j] = lst[i][j] + lst[i-1][j]
      else:
        lst[i][j] = lst[i][j] + min(lst[i-1][j],lst[i][j-1])

print lst[-1][-1]
print "time taken: " + str(time.time()-start)
