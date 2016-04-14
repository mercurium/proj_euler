import time
START = time.time()

SIZE = 10**8 * 5

def get_totient(size):  #gives you the totients of all numbers i <= size
  lst = range(1,size+1,2)
  lst[0] = 1
  for i in xrange(1,len(lst)):
    k = i*2+1
    if lst[i] == k:
      for j in xrange(i,len(lst),k):
        lst[j] = (lst[j] * (k-1))/k
  return lst

totients = get_totient(SIZE)

print sum(totients)
print "Time Taken:", time.time() - START



"""
f(n) = 0 if n % 2 == 0
f(n) = totient(n) if n % 2 == 1

10^5 = 2026413875
10^6 = 202642133233

2*i+1 = k
3k = 6*i+3

0 : 1
1 : 3
2 : 5
3 : 7
4 : 9
5 : 11
6 : 13
7 : 15

"""
