import string
import time
start = time.time()



triangles = []
for i in range(1,200):
  triangles = triangles + [i*(i+1)/2]
temp = open('prob42lst.txt','r')
lst = string.split(temp.read(),'","')
lst[0] = lst[0][1:]
triangle_count = 0

for i in range(0,len(lst)):
  str_sum = 0
  for j in range(0,len(lst[i])):
    str_sum = str_sum + ord(lst[i][j]) - 64
  if str_sum in triangles:
    triangle_count = triangle_count + 1
    print str_sum, lst[i]
    
print triangle_count    
print lst[1:3]

print "Time Taken: " + str(time.time()-start)

