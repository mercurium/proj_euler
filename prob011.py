import string
import time
START = time.time()

size = 20

temp = open('prob11lst.txt','r')
lst = string.split(temp.read(),'\n')

for i in xrange(0, len(lst)):
    lst[i] = string.split(lst[i],' ')

for i in xrange(0,size):
    for j in xrange(0,size):
        lst[i][j] = int(lst[i][j])
        
###############################
#### Processing Input above ###
###############################
        
maxz = 0

# Checking Rows
for i in xrange(0,size):
    for j in xrange(0, size-4):
        val = lst[i][j]*lst[i][j+1]*lst[i][j+2]*lst[i][j+3]
        if val > maxz:
            maxz = val

# Checking Columns
for i in xrange(0,size-4):
    for j in xrange(0, size):
        val = lst[i][j]*lst[i+1][j]*lst[i+2][j]*lst[i+3][j]
        if val > maxz:
            maxz = val

#Checking Diagonal Upper Left to Lower right
for i in xrange(0,size-4):
    for j in xrange(0, size-4):
        val = lst[i][j]*lst[i+1][j+1]*lst[i+2][j+2]*lst[i+3][j+3]
        if val > maxz:
            maxz = val
#Checking Diagonal Upper Right to Lower Left
for i in xrange(4,size):
    for j in xrange(0, size-4):
        val = lst[i][j]*lst[i-1][j+1]*lst[i-2][j+2]*lst[i-3][j+3]
        if val > maxz:
            maxz = val
print maxz

print "Time Taken:", time.time()-START
