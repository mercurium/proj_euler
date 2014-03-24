import time
start = time.time()

SIZE = 10**8


def gcd(a,b):
    while a != 0:
        a,b = b%a,a
    return b

def real_num(size):
    sumz = 0
    for i in xrange(1,size+1):
        sumz += (size//i) * i    
    return sumz    

def complex_num(size):
    sumz = 0
    squares = [x**2 for x in xrange(int(size**.5)+5)]
    for i in xrange(1,int(size**.5)+1):
        a = squares[i] 
        for j in xrange(i,size+1):
            b = squares[j] 
            if a + b > size:
                break
            for k in xrange(1,size+1):
                if k*(a+b) > size: 
                    break
                c = gcd(i,j)
                if c != 1: 
                    continue
                if i == j:
                    sumz += (2 * i * k) * (size/ ((a + b) * k ))
                else:
                    sumz += (2 * (i+j) * k) * (size/ ((a + b) * k ))
        print i, j
    return sumz    

def test():
    print "Test case for 5 is:",  (real_num(5) + complex_num(5) == 35 ) 
    print "Test case for 10^5 is:", (real_num(10**5)+ complex_num(10**5) == 17924657155 )

#test()
R = real_num(SIZE)
print "Time Taken: ", time.time() - start
C = complex_num(SIZE)
print "Total is:", R+C
print "Time Taken: ", time.time() - start

"""
This can be calculated by calculating the real_num numbers and the complex_num numbers separately. 
...except oh boy. This problem is harder than I expected.

If (1+2i) divides 5, then it also divides 10,15,20, etc... I forgot about that case... sigh....


Congratulations, the answer you gave to problem 153 is correct.

You are the 1203rd person to have solved this problem.

Total is: 17971254122360635
Time Taken:  458.844228029

In java... lololol... =/...
The answer for size 100000000 is: 17971254122360635
The time taken was: 20.288524384 seconds
"""
