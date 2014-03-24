import time
start = time.time()


count = 0
pr_sq = {4,9,25,49,121,169,289,361,529,841,961,1369,41**2,43**2,47**2}

for i in range(1,25+1):
    for j in pr_sq:
        if i%j == 0:
            count += 1
            break
print 25-count

