import time
start = time.time()

plst1 = [1]*4 + [0]*33
plst2 = [0]*37

clst1 = [1]*6+ [0]*31
clst2 = [0]*37

for k in range(1,9): #counting distribution of pete
  for i in range(1,5):
    for j in range(0,len(plst1)-i):
      plst2[i+j] += plst1[j]
  plst1 = plst2[:]
  plst2 = [0]*37



for k in range(1,6): #counting distribution of colin
  for i in range(1,7):
    for j in range(0,len(clst1)-i):
      clst2[i+j] += clst1[j]
  clst1 = clst2[:]
  clst2 = [0]*37

win = loss = 0
for colin in range(1,len(clst1)):
  for pete in range(1,len(plst1)):
    if pete > colin:
      win += clst1[colin] * plst1[pete]
    else:
      loss+= clst1[colin] * plst1[pete]

print win, loss
print win/(win+loss * 1.0)
print "Time Taken: " + str(time.time() -start)
