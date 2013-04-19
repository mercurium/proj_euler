import string

f = open('primenum10000.txt','r')

data = string.join(string.split(f.read(),',,'),',')
f = open('primenum10000.txt','w')
f.write(data)






#lst = range(2,1000000)

#i = 0
#while i < len(lst):
 # j = i+1
  #while j < len(lst):
   # if lst[j] % lst[i] == 0 and lst[i] != lst[j]:
    #  del lst[j]
   # else:
    #  j = j+1
  #i = i+1

#f.write(str(lst)[1:-1])
