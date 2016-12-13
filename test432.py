import time
start = time.time()

size = 10**2
mod = 10**9

def setup():
  lst = [0] + [1,2] * (size//2+1)
  for i in xrange(3,size+1,2):
    if lst[i] == 1:
      for j in xrange(i**2, size+1,2*i):
        if lst[j] == 1:
          lst[j] = i
      lst[i] = i
  return lst

pfactor_lst = setup()


def main():
  sumz = 0
  prev_seen = dict()
  for n in xrange(1,size+1):
    m = n
    temp = 1
    prev = 1
    while m != 1:
      if m in prev_seen:
        if  prev < 18:
          temp *= prev_seen[m]
        else:
          if m % prev == 0:
            temp *= prev_seen[m] * prev / (prev-1)
          else:
            temp *= prev_seen[m]
        m = 1
      elif pfactor_lst[m] < 18 or (prev == pfactor_lst[m]):
        temp *= pfactor_lst[m]
        m /= pfactor_lst[m]
      else:
        temp *= pfactor_lst[m]-1
        prev = pfactor_lst[m]
        m /= pfactor_lst[m]
    if n < size/2:
      prev_seen[n] = temp
    sumz += temp
  return sumz*92160

print "Time Taken:", time.time() - start, "(prime factorization found)"
print main()%mod
print "Time Taken:", time.time() - start, "finished entire job"
print #blank space



"""
This problem is... find S(510510,10^11) = sum( totient(510510 * n) for 1 <= n <= 10^11)

10^4 gives you: 4548570531840 at Time Taken: 0.0531239509583
10^6 gives you: 45480596821125120 at Time Taken: 9.45136904716
Time Taken: 4.7304019928 using the better method (sweet, 2x speedup :D)

Time Taken: 0.71129488945 is now my best time for 10^6 xD. Yay speedups...


"""



