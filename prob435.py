import time
START = time.time()
from math import factorial as fa
import math


def extended_gcd(a, b): #returns c,d such that ac+bd =1
	if b == 0:
		return (1, 0)
	else:
		q, r = a/b, a%b 
		s, t = extended_gcd(b, r)
		return (t, s - q * t)
ext_gcd = extended_gcd

def gcd(a,b):
	while b:
		a,b = b, a%b
	return a

def fibo(n,mod):
	def mmultiply(a,b):
		c = [[0,0],[0,0]]
		c[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0])%mod
		c[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1])%mod
		c[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0])%mod
		c[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1])%mod
		return c


	power_log2 = int(math.log(n,2)) 
	power_vals = [[[0,1],[1,1]]]
	for i in range(power_log2):
		power_vals.append(mmultiply(power_vals[-1],power_vals[-1]))
	
	power = n
	dig_mod2 = []
	for i in range(0,len(power_vals)):
		dig_mod2.append(power%2)
		power /= 2

	answer = [[1,0],[0,1]] 
	for i in range(0,len(power_vals)):
		if dig_mod2[i] == 1:
			answer = mmultiply(answer, power_vals[i])
	return answer[0][1]
	

SIZE = 100
n =  10**15
MOD =  fa(15) 
sumz = 0
for x in range(0,SIZE+1):
	mod = MOD * (x**2+x-1)
	num = (-x + pow(x,n+1,mod) * fibo(n+1,mod)  + pow(x,n+2, mod) * fibo(n,mod)) % (mod)
	denom = (x**2 + x - 1)
	if gcd(denom,fa(15)) == 1:
		sumz += num * ext_gcd(denom,fa(15))[0]
	elif num % denom == 0:
		sumz += num /denom
	else:
		num /=  gcd(denom, fa(15))
		denom /= gcd(denom,fa(15))
		denom = ext_gcd(denom, fa(15))[0]
		sumz += (num * denom) % MOD

sumz %= fa(15)

print sumz 
print fa(15)
print "Time Taken:", time.time() - START



"""
Using power series, we have F_n(x) = xF_n(x) + x^2F_n(x) + x - (x+x^2)F_n - x^2f_{n-1}(x) 
==> F_n(x) = (x - (x+x^2)f_n(x) - x^2(f_{n-1}(x)) ) / (1 - x - x^2)

so we need to find (1-x-x^2) mod w/e for x = 0 to 100
and f_n(x) = nth fibo num * x^n,
with fibo(0) = 0, fibo(1) = 1

The only hard part I ran into was moding too early. I figured out that in order to get the right answer, we need to find the top part mod (fa(15) * (x^2+x -1)) or else we might have the wrong result...
ex: 5x = 5 mod 15 has 5 solutions, x = 1,4,7,10,13
and only looking at it mod 15 doesn't give us the answer, but looking at it mod 75 would...

Congratulations, the answer you gave to problem 435 is correct.

You are the 283rd person to have solved this problem.

Return to Problems page.

21:58 ~/Desktop/python_projects/proj_euler $ python prob435.py
252541322550
1307674368000
Time Taken: 0.0367221832275

"""
