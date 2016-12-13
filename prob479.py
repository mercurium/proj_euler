import time, math
START = time.time()
SIZE  = 10**6
MOD   = 10**9+7

def ext_gcd(a, b): #returns c,d such that ac+bd =1
  if b == 0:
    return (1, 0)
  else:
    q, r = a/b, a%b
    s, t = ext_gcd(b, r)
    return (t, s - q * t)

sumz = 0
for x in range(1,SIZE+1):
  y     = 1 - x**2
  num   = ( (pow(y,SIZE+1,MOD) - y) * ext_gcd(y-1,MOD)[0]) % MOD
  sumz += num

print "Answer:", sumz % (10**9+7)
print "Time Taken:", time.time() - START

"""
Congratulations, the answer you gave to problem 479 is correct.
You are the 334th person to have solved this problem.

Return to Problems page.

Answer    : 191541795
Time Taken: 9.39927101135C


"""
