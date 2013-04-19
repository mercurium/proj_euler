import time
start = time.time()

size = 1008*3642
lst = [1]*(size+1)

for a in range(2,size+1,2):
  lst[a] *= 2
for a in range(4,size+1,4):
  lst[a] *= 2
for a in range(8,size+1,8):
  lst[a] *= 2
for a in range(16,size+1,16):
  lst[a] *= 2
for a in range(32,size+1,32):
  lst[a] *= 2
for a in range(64,size+1,64):
  lst[a] *= 2
  
  
for a in range(3,size+1,3):
  lst[a] *= 3
for a in range(9,size+1,9):
  lst[a] *= 3
for a in range(27,size+1,27):
  lst[a] *= 3
  
  
for a in range(7,size+1,7):
  lst[a] *= 7
for a in range(607,size+1,607):
  lst[a] *= 607


sumz = 0
for i in range(2,size):
  if lst[i] == 1 and lst[i-1] == 2:
    sumz+= i

print sumz
print count
print "Time Taken:", time.time() - start


"""
~/Desktop/python_projects/proj_euler $python prob182.py
399788195976 (total sum, the answer)
217800 (number of numbers that satisfy this)
Time Taken: 1.29034900665 (on desktop)
Time Taken: 0.115274554 (on java)
Let n = 1008*3642
N = 1009*3643

First I factored out (1008*3642), which came out to be:
[2, 2, 2, 2, 2, 3, 3, 3, 7, 607, 1]

Then I computed out gcd(i,n) by only caring about the factors of n, and multiplying the numbers that are divisible by it by e factors. The rest of them can be ignored.

Then we want gcd(e,n) = 1, like requested. The only time that 

m^e = m is when m^(e-1) = 1 mod N
m^b = 1 mod N only matters for numbers d|b such that d|n as well. So if gcd(b,n) = 2, we only have two messages that will be themselves. This means that we want to minimize gcd(e-1,n) while having gcd(e,n) = 1.

Basically, we can be butt lazy and just use that.

"""
