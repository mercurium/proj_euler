import string, time
start = time.time()
fileName = open('prob8input.txt','r')

number = fileName.read()
maxz = max(reduce(lambda x,y: int(x) * int(y), number[i:i+5], 1) \
            for i in range(len(number)-5))

print maxz
print "Time Taken: " + str(time.time()-start)

"""
read the values as a string, int-ify each digit, one at a time, compute product, return largest one
"""
