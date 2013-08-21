import string
import time

START = time.time()
input_data = open('data59.txt','r')
xor_chars = string.split(input_data.read(),',')

xor_chars = [int(xor_chars[i]) for i in xrange(len(xor_chars))]

sumz = 0
for i in xrange(0,len(xor_chars)):
	if i % 3 == 0:
		xor_chars[i] = xor_chars[i]^103
	elif i % 3 == 1:
		xor_chars[i] = xor_chars[i]^111
	else:	
		xor_chars[i] = xor_chars[i]^100
	sumz = sumz + xor_chars[i]

for i in xrange(0,len(xor_chars)):
	xor_chars[i] = chr(xor_chars[i])

print string.join(xor_chars,'')
print sumz

print "Time Taken:", time.time()-START
