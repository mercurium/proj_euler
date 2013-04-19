import time
start = time.time()

fib_val = [0,1]
i = 1
while fib_val[i] < 4000000:
  fib_val.append(fib_val[i] + fib_val[i-1])
  i = i+1
lst = [x for x in fib_val if x % 2 == 0]

print sum(lst)
print "Time Taken: " + str(time.time()-start)
