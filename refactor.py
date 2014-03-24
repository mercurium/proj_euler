import string, math

for i in range(1,500):
    fileString = "old" + '0' * (2 - int(math.log(i,10)))+ str(i) + ".py"
    try:
        fileRead = open(fileString, "r")
    except IOError:
        continue
    data = string.split(fileRead.read(),"	")
    fileRead.close()
    data = string.join(data,"    ")
    fileRead = open(fileString,"w")
    fileRead.write(data)
    fileRead.close()
    
    
