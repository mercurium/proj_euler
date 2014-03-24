from math import sqrt
import math
import time
start = time.time()

#answer was 661. The reason I was getting a wrong answer earlier was because I was looking at the loop variable i, rather than big_lst[i][1], which is the 'd' for the continued fraction.

def peller(lst): #returns h,k where we have h/k --> n
    if len(lst) == 1:
        return lst[0],1
    a = 1
    b = lst[-1]
    for j in xrange(len(lst)-2,0,-1):
        b_n = lst[j]*b+a
        a = b
        b = b_n
    a = a + lst[0]*b
    return a, b #this function adds up a_1+1/(a_2+1/(a3+...))
    

def convergents(lst, n): 
#this function finds the successive convergents of the list until h^2 - n *k^2 = 1
    for i in xrange(1,len(lst)+1):
        a,b = peller(lst[0:i])
        if a**2 - b**2 * n == 1:
            #print a, b, n, 'abbaa!'
            return a,b
    print 'ragequit your fault...'
    return -1,-1
    
    
#the way to get the next item in the list is such:
# A' = a*B -A
# B' = (d-A'*A')/B
# a' = int((sqrt(d)+A')/B')
def transform(A,B,a,d):
    A = a*B-A
    B = (d-A*A)/B
    a = int((sqrt(d)+A)/B)
    return A,B,a

big_lst = []
for d in xrange(2,1000): #iterate from 2 to 1000
    if int(sqrt(d+.2))**2 != d: #skipping squares
        new_inputs =transform(0,1,int(sqrt(d)),d) 
        lst_A =[new_inputs[0]]
        lst_B =[new_inputs[1]]
        lst_a =[new_inputs[2]] #this updates the list
        
        new_inputs =transform(lst_A[0],lst_B[0],lst_a[0],d)
        lst_A += [new_inputs[0]]
        lst_B += [new_inputs[1]]
        lst_a += [new_inputs[2]] #this updates the list again
        i=1
        while lst_A[-1]!=lst_A[0] or lst_B[-1]!=lst_B[0] or lst_a[-1] != lst_a[0]: #while it hasn't repeated yet...
            new_inputs =transform(lst_A[i],lst_B[i],lst_a[i],d)
            lst_A += [new_inputs[0]]
            lst_B += [new_inputs[1]]
            lst_a += [new_inputs[2]]
            i+=1 #our fancy loop counter
        big_lst +=    [([int(sqrt(d))] + lst_a[:-1]*20, d)]

maxz = 0
max_n = 0
for i in xrange(0,len(big_lst)):
    a, b = convergents(big_lst[i][0], big_lst[i][1])
    #print a,b, big_lst[i][1], 'RAAAH'
    if a > maxz:
        maxz = a
        max_n = big_lst[i][1]
        #print a , b, big_lst[i][1]
print "Max is:", max_n
print "Time Taken:", time.time() - start

