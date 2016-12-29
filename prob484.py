import time
START = time.time()


def pfactor_gen(size): #for each number n, return some factor of it.
  factors = [0,1,2] + [1,2] *(size/2-1)
  for i in xrange(3,size,2):
    if factors[i] == 1:
      for j in xrange(i**2,size,i*2):
        factors[j] = i
      factors[i] = i
  return factors


print "Time Taken:", time.time() - START


"""
n = (p_1^{m_1}p_2^{m_2}...p_k^{m_k})
gcd(n, n') = ((p_1)^{m_1-1} p_2^{m_2-1} ... p_k^{m_k-1}) * (any p_i where p_i | m_i)
gcd(p^p *n , (p^p *n)') = p^p * gcd(n,n')


"""
