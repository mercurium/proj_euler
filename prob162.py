from math import factorial

def nCr(n,r):
  return factorial(n)/factorial(r)
  
sum2 = 0
for i in range(2,16):
  sum2 = sum2 + 15**i - 2 * 14**i + 13**i

c = 16**16-15**16*3 + 14**16 *3 - 13**16

print hex(sum2)
print hex(16**16-15**16*3 + 14**16 *3 - 13**16)

print hex(c - sum2) #this is the answer :D :D :D 
