import time
start = time.time()

data = open('data185.txt','r')
data = data.read()

guesses = data.split()[::2]
correct = data.split()[1::2]

for i in range(len(correct)):
  correct[i] = int(correct[i])
  
print guesses, correct

a = [0]*16
c = []
count = 0

for a[0] in range(0,10):
  c.append(correct[:])
  for i in range(len(guesses)):
    if guesses[i][0] == str(a[0]): c[0][i] -= 1
    
  if min(c[0]) >= 0:
    for a[1] in range(0,10):
      c.append(c[0][:])
      for i in range(len(guesses)):
        if guesses[i][1] == str(a[1]):
          c[1][i] -= 1
          
      if min(c[1]) >= 0:
        
        for a[2] in range(0,10):
          c.append(c[1][:])
          for i in range(len(guesses)):
            if guesses[i][2] == str(a[2]):
              c[2][i] -= 1
          if min(c[2]) >= 0:
            count += 1
          c.pop(2)        
      c.pop(1)
  c.pop(0)
  
print count  
print "Time Taken:", time.time()-start
  
  
  
  
  
  
  
