import time, string
START = time.time()

cubeLst = {}

for i in range(0,10000):
    m = string.join(sorted(str(i**3) ),'' )
    if m in cubeLst:
        cubeLst[m] += [i]
    else:
        cubeLst[m] = [i]
    if len(cubeLst[m]) == 5:
        print min(cubeLst[m])**3, min(cubeLst[m])
        break
print "Time Taken:", time.time() -START
