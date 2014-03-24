import time
START = time.time()
from bitarray import bitarray

size = 10**6

seen_before = bitarray('0' * size)
divs = [1]*size
for i in xrange(2,len(divs)):
    for j in xrange(2*i,len(divs),i):
        divs[j]+=i

chain_len = dict()

def calc(num):

    if num > size or (num not in chain_len and divs[num] in chain_len):
        chain_len[num], seen_before[num] = 0,1
    if seen_before[num]: return

    #else if num < size and not seen before...
    val = divs[num]
    while val < size and not seen_before[val]:
        seen_before[val] = 1
        val = divs[val]
    if val > size or val in chain_len: #if the value exceeds the size, they're all dq'd
        chain_len[num] = 0
        val = divs[num]
        while val not in chain_len and val < size:
            chain_len[val] = 0
            val = divs[val]
        return
                
    elif val < size and seen_before[val]:
        count = 0
        seen_set = set([])
        while val not in seen_set:
            seen_set.add(val)
            val = divs[val]
            count +=1
        for item in seen_set:
            chain_len[item] = count


for i in xrange(0,size):
    calc(i)
maxz,maxkey = 0,0
for key in chain_len.keys():
    if chain_len[key] > maxz:
        maxz = chain_len[key]
        maxkey = key
        
print maxz, maxkey
print "Time Taken:", time.time() - START
