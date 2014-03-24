import sys, time
START = time.time()

num_to_factor = int(sys.argv[1]) if len(sys.argv) > 1 else 600851475143


def factor(val):
    def factor_rec(val, count):
        while(val >= count):
            if val % count == 0:
                 return count
            count = count + 1

    if val == 1:
        return [1]
    temp = factor_rec(val, 2)
    return [temp] + factor(val/temp) 

print factor(num_to_factor)[:-1]
print "Time Taken:", time.time()-START 

"""
not a very hard problem if you consider that you *only* AT MOST need to check ~2.4 million divisions, much less in the actual case, and quite a few less if you do some preprocessing to find the prime numbers first. I have a better prime factorization algorithm (though it's stil pretty bad) and a prime checking algorithm under primes.py and miller_rabin.py
"""
