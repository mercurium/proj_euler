import time
start = time.time()

lst = [1]*20
num_mod = 20092010


for i in xrange(20,1000):
  lst.append((lst[i-20] + lst[i-19])%num_mod)

print lst[-10:]
print "Time Taken:", time.time() - start
