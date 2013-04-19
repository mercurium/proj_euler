import string
file = open('carmichael.txt','r')

lst = string.split(file.read(),'\n')[:-1]


for i in range(0,len(lst)):
  lst[i] = int(lst[i])
print lst
