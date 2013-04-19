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
found = False

def base_case():
  for a[15] in range(0,10):
    c.append(c[14][:])
    for i in range(len(guesses)):
      if guesses[i][15] == str(a[15]):
        c[15][i] -= 1
      if min(c[15]) >= 0:
        print c[15]
        found = True
  c.pop(15)
  return

def recurse(level):
  if level == 8: print a
  for a[level] in range(0,10):
    if found == True:
      return
    c.append(c[level - 1][:])
    for i in range(len(guesses)):
      if guesses[i][level] == str(a[level]):
       c[level][i] -= 1
    if min(c[level]) >= 0:
      if level < 15:
        recurse(level+1)
      else:
        base_case()
  c.pop(level)


for a[0] in range(0,10):
  c.append(correct[:])
  for i in range(len(guesses)):
    if guesses[i][0] == str(a[0]): c[0][i] -= 1
    
  if min(c[0]) >= 0:
    recurse(1)
  c.pop(0)

print "Time Taken:", time.time()-start
  
  
  
  
  
  
  
