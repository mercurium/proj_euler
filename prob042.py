import string
import time
START = time.time()



triangles = set( [ (i*(i+1)/2) for i in range(1,200)] )  #Set of triangle numbers to save on time later.
data = open('data42.txt','r')
words = string.split(data.read(),'","')

words[0] = words[0][1:] #Getting rid of a " left over from input.
triangle_count = 0

for word in words: 
    str_sum = sum( [ (ord(word[letter]) - 64) for letter in range( 0,  len(word) )  ] )
    if str_sum in triangles:
        triangle_count = triangle_count + 1
        #print str_sum, words[i]
        
print triangle_count        
print "Time Taken:", time.time() - START
