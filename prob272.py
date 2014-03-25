#NOTE TODO need to solve it
import time
START = time.time()
from bitarray import bitarray

LIM = 10**6*2
MAX_SIZE = 10**11

def get_suitable_nums(LIM):
    is_prime = bitarray('001' + '10' * (LIM/2) )[:LIM]
    for i in xrange(3,LIM,2):
        if is_prime[i]:
            if i**2 > LIM: continue
            for j in xrange(i**2,LIM,2*i):
                is_prime[j] = 0
    prime_lst = []
    for i in xrange(7,LIM,6):
        if is_prime[i]:
            prime_lst.append(i)
    return prime_lst

prime_lst = get_suitable_nums(LIM)

print len(prime_lst)    
print prime_lst[:10]

sumz = 0
loop_count =0

#Lazy man's implementation...
for a in xrange(len(prime_lst)):
    break
    item1 = prime_lst[a]
    for b in xrange(a+1,len(prime_lst)):
        item2 = prime_lst[b]
        if item1*item2**4 > MAX_SIZE:
            break
        for c in xrange(b+1,len(prime_lst)):
            item3 = prime_lst[c]
            if item1 * item2 * item3**3 > MAX_SIZE:
                break
            for d in xrange(c+1,len(prime_lst)):
                item4 = prime_lst[d]
                if item1 * item2 * item3 * item4**2 > MAX_SIZE:
                    break
                for e in xrange(d+1,len(prime_lst)):
                    item5 = prime_lst[e]
                    if item1 * item2 * item3 * item4* item5 > MAX_SIZE:
                        break
                    sumz += item1 * item2 * item3 * item4 * item5
                    loop_count +=1
                    print "hurr", loop_count, a,b,c,d,e
    print a, item1
print sumz
                    


print "Time Taken:", time.time() - START
