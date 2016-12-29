#NOTE TODO need to solve it

a,b = 2,7
ulam = [a,b]
vals = dict()
vals[a+b] = 1
for i in range(30):
    for nextVal in range(ulam[-1]+1, ulam[-1]*2):
        if nextVal in vals and vals[nextVal] == 1:
            for num in ulam:
                if num + nextVal in vals:
                    vals[num+nextVal] +=1
                else:
                    vals[num+nextVal] = 1
            ulam.append(nextVal)
            break
print ulam


"""
a,b = 2,5

2, 5, 2+5,2(2) + 5, 3(2)+5, 5(2)+5, 3(2)+2(5), 6(2)+5, 7(2)+5, 8(2)+5, 5(2)+3(5), 


"""
