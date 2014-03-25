import time
START = time.time()

def reverse(num):
    return int(str(num)[::-1])

count = 0
for i in range(1,10000):
    lychrel = True
    n = i
    for j in range(1,51):
        n = n+reverse(n)
        if n == reverse(n):
            lychrel = False
            break
    count = count+lychrel

print count
print "Time Taken:", time.time() - START
