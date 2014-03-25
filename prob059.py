import string, time

START = time.time()
fileRead = open('prob59lst.txt','r')
charString = string.split(fileRead.read(),',')

counter = {}
charString = [int(char) for char in charString]

sumz = 0
for i in xrange(0,len(charString)):
    if i % 3 == 0:
        charString[i] = charString[i]^103
    if i % 3 == 1:
        charString[i] = charString[i]^111
    if i % 3 == 2:
        charString[i] = charString[i]^100
    sumz = sumz + charString[i]

charString = string.join([chr(charString[i]) for i in range(len(charString))], '')

print charString
print sumz
print "Time Taken:", time.time()-START
