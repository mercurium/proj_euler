import string
import time
START = time.time()

prime_check_list = [1]*20162 # We can use this limit because of the given value on the website.
for i in xrange(2,len(prime_check_list)):
    for j in xrange(2*i,len(prime_check_list),i):
        prime_check_list[j] += i
abu = set()
for i in xrange(12,len(prime_check_list)):
    if prime_check_list[i] > i:
        abu.add(i)
        
print len(abu)
abu = list(abu)
abu.sort()
non_abundant_nums = set()


for i in xrange(0,len(abu)):
    for j in xrange(i,len(abu)):
        if abu[i]+abu[j] > 20162:
            break
        non_abundant_nums.add(abu[i]+abu[j])
non_abundant_nums = list(non_abundant_nums)

print 20162*20163/2 - sum(non_abundant_nums)
print "Time Taken:", time.time() - START
