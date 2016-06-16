import time,math
from bitarray import bitarray
START = time.time()


val = 1234567890
sumz = 0
MOD = 10**18
SIZE = 10**4

#Generic Sieve of Eratosthenes 
def getPrimeSet(size): 
    prime_set = set([2])
    is_prime = bitarray('1'*size)
    for i in xrange(3,len(is_prime),2): 
        if is_prime[i]:
            prime_set.add(i)
            for j in xrange(2*i,len(is_prime),i):
                is_prime[j]= False
    return prime_set

def isPrime(n):
    return n in prime_set

def estimate(n,val,base): #Compute an upper bound for how big the number can be
    n /= base
    sumz = 0
    while n != 0:
        sumz +=n
        n/=base    
    expected = sumz * val

    return expected * (base-1) + base*20

def correctingVals(correction, base):
    val_check = 0
    for i in xrange(1,int(math.log(correction,base)+1) ):
        val_check += correction / base**i
    return val_check

def cfpn(n, val, base): #Compute For Power of Number 
    p = base
    sumz = 0
    comp = base
    while comp <= n:
        sumz += n/comp
        comp *= base
    expected = sumz * val


    #This is the estimate of our answer, however it's not always right...
    valz = expected * (base-1) + (expected % base)  

    #checking to see how much we're off by...
    val_check = sum([valz/base**i for i in xrange(1,int(math.log(valz,base)+1) ) ])  
    correction = valz + (expected - val_check) * (base-1)
    correction += (-1 * correction)%base    

    #and a second check...
    val_check2 = correctingVals(correction, base)

    if val_check2 == expected:
        return correction
    diff = val_check2 - expected

    while diff > 0: #Adjusting our value down, we got a power higher than needed
        if correction % (p**(diff+1)) == 0:
            return correction
        correction -= base
        val_check2 = correctingVals(correction, base)
        diff = val_check2 - expected

    while diff < 0: #Adjusting our value up, we got a power lower than we need.
        correction += base
        val_check2 = correctingVals(correction, base)
        diff = val_check2 - expected

    return correction

def figure_out_possible_expensive_primes(size):
    plst = prime_lst[:40]

    for num in xrange(1,int(i**(1/3.)) ):  # Figuring out the prime powers that we need to check.
        potential_most_expensive_prime = i/num

        if isPrime(potential_most_expensive_prime) and i%potential_most_expensive_prime == 0: 
            plst.append(potential_most_expensive_prime)

        a = prime_lst[least_prime_sqrt[potential_most_expensive_prime] - 1]
        b = prime_lst[least_prime_sqrt[potential_most_expensive_prime] - 2]

        if i%a == 0:
            plst.append(a)
        if i%b == 0:
            plst.append(b)

    return plst

prime_set = getPrimeSet( int(SIZE * 1.1))
prime_lst = sorted(prime_set)

index = 0
least_prime_sqrt = [0] * (SIZE+1)
lp_sq = [0] * (SIZE+1)
#I slightly regret this implementation, but this gives you the largest prime < sqrt(n)
for i in xrange(len(least_prime_sqrt)):  
    if i**.5 >= prime_lst[index]:
        index+=1
    least_prime_sqrt[i] = index

print "Time Taken:", time.time()- START


expensive_loop_count = 0
total_loop_count = 0
sumz = 0
minimum_potential_cost = 0    
most_expensive_prime = 2

for i in xrange(10,SIZE+1):
    if i%1024 == 0:
        print i

    if isPrime(i): #For primes p, we know that p is going to give the largest power that we need.
        most_expensive_prime = i
        minimum_potential_cost = cfpn(i,val,i) 
        total_loop_count +=1
        expensive_loop_count +=1

    else:
        plst = figure_out_possible_expensive_primes(i)
        for prime in plst: 
            total_loop_count +=1
            #shortcut compute some values so we don't have to do all of them.
            if estimate(i,val,prime) < minimum_potential_cost: 
                continue #computations skipped :)

            temp = cfpn(i,val,prime) #This function is more costly...
            expensive_loop_count +=1 
            if temp >= minimum_potential_cost:
                minimum_potential_cost = temp
                most_expensive_prime = prime


    sumz= (sumz + minimum_potential_cost) % MOD

print sumz
print "Time Taken:", time.time()- START

print "damn, that was:", expensive_loop_count, "loops..."
print "total loop count was", total_loop_count
