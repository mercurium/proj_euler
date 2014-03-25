#NOTE TODO need to solve it
import time
start = time.time()
import sys



SIZE = 10**6 if len(sys.argv) == 1 else int(sys.argv[1])
MOD = 10**9

def setup():
    lst = [0] + [1,2] * (SIZE//2+1)
    for i in xrange(3,SIZE+1,2):
        if lst[i] == 1:
            for j in xrange(i**2, SIZE+1,2*i):
                if lst[j] == 1:
                    lst[j] = i
            lst[i] = i
    return lst

pfactor_lst = setup()

def pfactor(n):
    if n == 1:
        return []
    if n > SIZE:
        return "too big, fool"
    if n == pfactor_lst[n]:
        return [n]
    factors = []
    while n > 1:
        factors.append(pfactor_lst[n])
        n /= pfactor_lst[n]
    return factors

def main():
    c1,c2,c3,c4,c5 = 0,0,0,0,0
    sumz = 0
    prev_seen = dict()
    for n in xrange(1,SIZE+1):
        if n%2 == 0:
            a = prev_seen[n/2] * 2
            if n <= SIZE/2: prev_seen[n] = a
            sumz +=a
            continue
        if n%3 == 0:
            a = prev_seen[n/3] * 3
            if n <= SIZE/2: prev_seen[n] = a
            sumz+=a
            continue
        if n%5 == 0:
            a = prev_seen[n/5] * 5
            if n <= SIZE/2: prev_seen[n] = a
            sumz+=a
            continue
        if n%7 == 0:
            a = prev_seen[n/7] * 7
            if n <= SIZE/2: prev_seen[n] = a
            sumz+=a
            continue
        if n%11 == 0:
            a = prev_seen[n/11] * 11
            if n <= SIZE/2: prev_seen[n] = a
            sumz+=a
            continue
        m = n
        temp = 1
        prev = 1
        while m != 1:
            if m in prev_seen:
                if  prev < 18:
                    temp *= prev_seen[m]
                    c1+=1
                else:
                    if m % prev == 0:
                        temp *= prev_seen[m] * prev / (prev-1)
                        c2+=1
                    else:
                        temp *= prev_seen[m] 
                        c3+=1
                m = 1
            elif pfactor_lst[m] < 18 or (prev == pfactor_lst[m]):
                temp *= pfactor_lst[m]
                m /= pfactor_lst[m]
                c4+=1
            else:
                temp *= pfactor_lst[m]-1
                prev = pfactor_lst[m]
                m /= pfactor_lst[m]
                c5+=1
        if n < SIZE/2:    prev_seen[n] = temp
        sumz += temp
    total_reps= tr = c1+c2+c3+c4+c5
    print c1,c2,c3,c4,c5, total_reps
    print round(c1*1.0/tr,4), round(c2*1.0/tr,4),round(c3*1.0/tr,4),round(c4*1.0/tr,4), round(c5*1.0/tr,4)
    return sumz*92160

print "Time Taken:", time.time() - start, "(prime factorization found)"
print main()
print "Time Taken:", time.time() - start, "finished entire job"
print #blank space



"""
This problem is... find S(510510,10^11) = sum( totient(510510 * n) for 1 <= n <= 10^11)

10^4 gives you: 4548570531840 at Time Taken: 0.0531239509583
10^6 gives you: 45480596821125120 at Time Taken: 9.45136904716
Time Taken: 4.7304019928 using the better method (sweet, 2x speedup :D)

Time Taken: 0.71129488945 is now my best time for 10^6 xD. Yay speedups...


"""



