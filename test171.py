squares = [x**2 for x in range(1,200)]

count = 0
vals = dict()
for i in xrange(1,100):
	val = sum([int(x)**2 for x in str(i)])
	if val in squares:
		vals[val] = vals[val]+ [i] if val in vals else [i]
		count +=i

#for key in vals:
#	print key, vals[key]
print count
