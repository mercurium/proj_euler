import time
start = time.time()
from math import log
import string

#largest digit in lst[0]
def base14(num):
    base = ''
    while num != 0:
        n = num%14
        if n > 9: n = chr(n+87)
        n = str(n)
        base = n + base
        num/=14
    return base

#largest digit in lst[0]
def base14lst(num):
    base = [0]*10000
    for slot in range(10000):
        n = num%14
        base[slot] = n
        num/=14
    return base[::-1]


n1 = 7
n2 = 8
sumz = 1
for dig in xrange(1,10000):
    base = 14**dig
    for i in xrange(0,14):
        val = base*i+n1
        if val**2 % (base*14) == val:
            n1 = val
            break
    for i in xrange(0,14):
        val = base*i+n2
        if val**2 % (base*14) == val:
            n2 = val
            break
    print dig

print "Time Taken:", time.time() - start

lst1 = base14lst(n1)
lst2 = base14lst(n2)

c1,c2 = 1,1
for i in xrange(0,len(lst1)):
    if lst1[i] != 0:
        sumz += c1*lst1[i]
        c1+=1
    if lst2[i] != 0:
        sumz += c2*lst2[i]
        c2+=1


print '\n', sumz, base14(sumz)
print "Time Taken:", time.time() - start


"""
Since adding the digits together is slowing my program down too much... I'll do it at the end and only do it once :x...


604558007 5a411d7b
Time Taken: 248.282007933
Time Taken: 140.645628929 (improved to this after breaking if i found the number i needed.)

Strategy for this problem: I noticed that in order for a number to be i^2 = i mod 14^k, we have to have i^2 = i mod 14^k (duh right? xD). This means that we could keep building the digits starting with 1 digit numbers and incrementing all the way up to 10,000 digits.

My original program took forever because I tried summing up the number's digits as I was going. This was remedied by summing them all up at the end.


One final mistake. I was originally going to iterate through n = 1 to 10000 and thus i had sum start out at 15 (= 7+8), since i was skipping the 10^0th digit. Then later when I fixed my summing problem, I missed this and it caused a bit of fail for me. Maybe I should scrap code when I rewrite functions...
"""




