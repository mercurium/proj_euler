import time
import math
start = time.time()


#finds the first 85 fibonacci numbers... lol. not bad :D
fibo = [1] * 85
for i in range(2,len(fibo)):
  fibo[i] = fibo[i-1]+fibo[i-2]

fibo_t = [0,0,1,2,5]+[0]*85
for i in range(3,len(fibo_t)):
  fibo_t[i] = fibo_t[i-1]*2 + fibo_t[i-2] - 2* fibo_t[i-3] - fibo_t[i-4]
#Here's where we do the real work for computing sum of z(n)
sumz = extra = 0
val = 10**17-1
while val != 0:
  for i in range(len(fibo)-1,0,-1):
    if val >= fibo[i]:
      val -= fibo[i]
      sumz += fibo_t[i] + fibo[i]* extra+1
      #print sumz, val + fibo[i],extra
      extra += 1

print sumz
print "Time elapsed = " + str(time.time()-start)

#okay, so I realized that it has to do with this one sequence on the integer sequence database... http://oeis.org/A001629
#and so the formula is fibo_t[i] = fibo_t[i-1]*2 + fibo_t[i-2] - 2* fibo_t[i-3] - fibo_t[i-4]


#So my idea (that isn't working yet....) is to subtract the largest value of fibo_t from the number while that number is still bigger than those the fibonacci number. This can be used to compute z(n) waaaay faster than doing it stupidly...


#OKAY. So the reason it wasn't working was because i was multiplying by the wrong number... =.=;;
