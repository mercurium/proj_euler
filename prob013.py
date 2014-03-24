import string,time
fileRead = open('prob13number_list.txt','r')
START = time.time()

strz = fileRead.read()
number_list = string.split(strz.strip(), '\n')
sumz = sum([ int(x) for x in number_list])
    
print str(sumz)[:10] 

print "Time Taken:", time.time() - START
