import string

for i in range(100,460):
    fileRead = open("prob"+str(i)+".py", "r")
    data = string.split(fileRead.read(),"	")
    fileRead.close()
    print data
    data = string.join(data,"    ")
    print data
    fileRead = open("prob"+str(i)+".py", "w")
    fileRead.write(data)
    fileRead.close()
    
    
