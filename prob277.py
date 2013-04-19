import time
start = time.time()


def extended_gcd(a, b): #returns c,d such that ac+bd =1
  if b == 0:
    return (1, 0)
  else:
    q, r = a/b, a%b
    s, t = extended_gcd(b, r)
    return (t, s - q * t)
ext_gcd = extended_gcd

a,b,denom = 1,0,1

def U(a,b,denom):
	a = 4*a
	b = denom*2+4*b
	denom *= 3
	return a,b,denom

def D(a,b,denom):
	return a,b,denom*3

def d(a,b,denom):
	a=2*a
	b = 2*b - denom
	denom *= 3
	return a,b,denom


seq =    "UDDDUdddDDUDDddDdDddDDUDDdUUDd"

for letter in seq:
	if letter == 'U':
		a,b,denom = U(a,b,denom)
	if letter == 'D':
		a,b,denom = D(a,b,denom)
	if letter == 'd':
		a,b,denom = d(a,b,denom)
	#print a,b,denom

print a,b,denom

vals = (ext_gcd(a,denom)[0] * -1*b) %denom
print vals

while vals < 10**15:
	vals += denom
print vals
print "Time Taken:", time.time() - start


"""
1125977393124310
Time Taken: 0.000288009643555
Time Taken: 8.01086425781e-05 (without the print statements)

Basic idea, apply changes to numbers that happened at each iteration, we get a number

(an+b)/denom. We need some n such that this works.
Answer: find a*n-denom*m = 1, multiply by -b, and mod it by the denominator to get the smallest possible answer.

Then if A is a solution, so is A + denom, or A +2*denom, etc. Then we just need to find A + n*denom > 10**15.

"""
