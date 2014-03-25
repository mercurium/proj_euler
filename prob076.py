import time

START = time.time()
SIZE = 100
partitionNK = {(1,1):1, (0,0):1}

def partitions(n):
    def partitionNK(n,k):
        if (n,k) in partitionNK: #memoize, don't repeat work.
            return partitionNK[(n,k)]
        elif n == k: #if n ==k, only one way
            return 1
        elif n < k or n <= 0 or k <= 0: #none of these are valid, so 0
            return 0
        partitionNK[(n,k)] = partitionNK(n-1,k-1) + partitionNK(n-k,k)
        return partitionNK[(n,k)]

    return sum([partitionNK(n,k) for k in xrange(1,n+1)])
    

print partitions(SIZE) -1
print "Time Taken:", time.time() - START

"""
Definition: partition(n,k) = number of ways to partition n into k parts, order does NOT matter.

So the entire problem relies on the fact that:
partition(n,k) = partition(n-1,k-1) + partition(n-k,k)

Since order doesn't matter for partitions, all partitions can be grouped into those that have all individual parts > 1, in which case the number of those = paritition(n-k,k), and those with at least one part = 1, with number = partition(n-1,k-1). Thus, we can use the sum as stated

"""
