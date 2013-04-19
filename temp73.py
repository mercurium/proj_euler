size =8
items = set()

lst = [x for x in range(0,size+1)]


for i in range(2,len(lst)):
  if lst[i] == i:
    for j in range(i,len(lst),i):
      lst[j] *= (i-1.0)/i

sumz = 0
for i in range(2,len(lst)):
  sumz+= lst[i]
print lst, sumz
##################################
lst = range(0,9)
for i in range(2,len(lst)):
  if lst[i] ==i:
    for j in range(i,len(lst),i):
      lst[j] *= (i-1.0)/i
#print lst
total = sum(lst)-1
print total/6., total






########################################
lst_new = lst[:]
i = 0
while primes[i] < len(lst):
  for n in range(primes[i]+1,len(lst)):
    lst_new[n] = lst[n] + lst[n-primes[i]]
    if n==10:
      print n, primes[i]
      lst = lst_new[:]
  i+=1

maxz = 0
for i in range(0,len(lst)):
  if maxz < lst[i]:
    print i, lst[i]
    maxz = lst[i]
print range(0,len(lst))
print lst
