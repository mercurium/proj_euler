### NOTE Not sure why this file exists.... once I confirm that deleting it won't have any bad effects, I'm going to remove it

import string
import time

start = time.time()

temp = open('primenum10000.txt','r')
primes_few = string.split(temp.read(),',')
for i in range(0,len(primes_few)):
	primes_few[i] = int(primes_few[i])
	

def factor_rec(val, count):
	while(val >= count):
		if val % count == 0:
			 return count
		count = count + 1

def factor(val):
	if val == 1:
		return [1]
	temp = factor_rec(val, 2)
	return [temp] + factor(val/temp)
	
def sum_pow(n, pow):
	sum = 0
	for i in range(0,pow+1):
		sum = sum + n**i
	return sum
	
def sum_div(val):
	lst = factor(val)
	term = 1
	prod = 1
	count = 0
	while lst[0] != 1:
		if lst[0] == term:
			count = count + 1
			del lst[0]
		elif lst[0] != term:
			prod = prod * sum_pow(term, count)
			term = lst[0]
			count = 1
			del lst[0]
	prod = prod * sum_pow(term,count)
	return prod
		
def s_d(val):
 return sum_div(val) - val
		
count = 0
sum = 0
for i in range(1,10000):
	n = s_d(i)
	if n != 0:
		ni = s_d(n)
		if n != i and ni == i:
			count = count +1
			sum = sum +i
print sum
print "time taken: " +str(time.time()-start)		

