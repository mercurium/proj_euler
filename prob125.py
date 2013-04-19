import time
import string
start = time.time()
#2906969179, there's two duplicates.
#run time of 1.116 seconds :D

lst =range(0,10**4+1)
ans = set()
for i in range(0,len(lst)):
  lst[i] = lst[i]*(lst[i]+1)*(2*lst[i]+1)/6


for i in range(2,len(lst)):
  for j in range(i-2, -1, -1):
    n = lst[i]-lst[j]
    if n > 10**8:
      break
    if str(n) == str(n)[::-1]:
      ans.add(n)

ans =list(ans)
print sum(ans),len(ans)

print "Time Taken: " + str(time.time()-start)












