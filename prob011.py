import string
import time
START = time.time()

size = 20

temp = open('prob011lst.txt','r')
lst = string.split(temp.read(),'\n')

for i in xrange(0, len(lst)):
    lst[i] = string.split(lst[i],' ')

for i in xrange(0,size):
    for j in xrange(0,size):
        lst[i][j] = int(lst[i][j])
        
###############################
#### Processing Input above ###
###############################

def prod(array):
    product = 1
    for element in array:
        product *= element
    return product
        
maxz = 0

# Checking Rows
for i in xrange(0,size):
    for j in xrange(0, size):
        val = prod(lst[i][j:j+4])
        maxz = max(val, maxz)

# Checking Columns
for i in xrange(0,size-3):
    for j in xrange(0, size):
        val = lst[i][j]*lst[i+1][j]*lst[i+2][j]*lst[i+3][j]
        maxz = max(val, maxz)

#Checking Diagonal Upper Left to Lower right
for i in xrange(0,size-3):
    for j in xrange(0, size-3):
        val = prod( [lst[i+x][j+x] for x in range(4) ] )
        maxz = max(val, maxz)

#Checking Diagonal Upper Right to Lower Left
for i in xrange(3,size):
    for j in xrange(0, size-3):
        val = lst[i][j]*lst[i-1][j+1]*lst[i-2][j+2]*lst[i-3][j+3]
        maxz = max(val, maxz)
print maxz

print "Time Taken:", time.time()-START
