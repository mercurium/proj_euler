import string
import time
start = time.time()
from math import sqrt, log



#lastn = 27304197
#ratio = 5.8284266094

lastn = 4
ratio = 1

nextz = int(lastn * ratio)
num = int((.5)**.5 * nextz)
while lastn < 10**13:
	num = int(.5**.5 * nextz)
	while num*(num+1)*2 < nextz * (nextz+1):
		num = num+1
	if num*(num+1)*2 == nextz * (nextz+1):
		print num+1, '/', nextz+1, log(nextz+1,10)
		ratio = (nextz+1)*1./lastn
		lastn = nextz+1
		nextz = int(lastn * ratio)
	else:
		nextz +=1

print "Time Taken: " + str(time.time() - start)



"""
756872327473 / 1070379110497 5.82842712467 12.0295376248
Time Taken: 0.000450134277344
So I realized (from running the program on small inputs) is that the ratio of solutions is approximately 5.828 (with fluctuation since it's not an integer), which means if we only check the powers of 5.828 * starting num, we only need to iterate through... maybe 20 numbers and the error margin that we have? It's not too bad and the runtime is fast too xD.

Actually, looking at how many times i had to increment, it was probably less than 20 times/new number, which means that I only had to do a digit check for ~400 numbers o.O... no wonder it was that fast xD

vals2 = dict()

lastn = 1
for i in xrange(1,N):
	n = i*(i-1)
	if n in vals2:
		print vals2[n], '/',i, i*1./lastn
		lastn = i
	vals2[2*n] = i

3 / 4 4.0
15 / 21 5.25
85 / 120 5.71428571429
493 / 697 5.80833333333
2871 / 4060 5.82496413199
16731 / 23661 5.82783251232
97513 / 137904 5.82832509192
568345 / 803761 5.82840961829
3312555 / 4684660 5.8284241211
19306983 / 27304197 5.8284266094

"""

