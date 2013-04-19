import string
def count_dig(n):
  n = str(n)
  sum = 0
  for i in range(0,len(n)):
    if n[i] != 'L':
      sum += int(n[i])
  return sum

max = 0
max_i, max_j = 0,0
for i in range(50,100):
  for j in range(50,100):
    n = i**j
    mn = count_dig(n)
    if max < mn:
      max = mn
      max_i,max_j = i,j
print max, max_i,max_j


