#NOTE TODO need to solve it
import time
start = time.time()
from math import factorial as fa, log
from primes import ncr

lim = 10**15

def fat(n):
    if n == 0 or n==1:
        return 0
    return fa(n)

def f(m,n):
    val = (ncr(m*n,n-1)+n-1)/n
    val2 = fa(n*m-n)/(fa(n)**(m-1))
    val3 = fa(m-1)
    print m,n, 'hii', val,val2,val3, round(log(val*val2-val3,10),2), val*val2-val3
    return val*val2-val3

#really only meant for n = 2, testing if f(m,n) performs as I want it to
def test(m,n): 
    return m* fa(2*m-2)/(2**(m-1)) - fa(m-1)

def main():
    sumz = 0
    m,n = 2,2
    
    a = f(m,n)
    while a < lim:
        while a < lim:
            sumz += a
            m+=1
            a = f(m,n)
        print m,n, 'failed'
        m = 2
        a = f(m,n)
        n+=1
    for i in xrange(0,40):
        if fa(i) < lim:
            sumz += fa(i)
        else:
            break
    return sumz        

"""
Okay, I didn't solve it but my reasoning for the formula in f(m,n) is that I noticed 


"""
