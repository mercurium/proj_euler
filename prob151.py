import time
start =time.time()
import string

vals = [0]*17
for i in range(1,17): vals[i] = dict()

vals[16][(1,0,0,0,0)] = 1

vals[15][(0,1,1,1,1)] = 1

for numPapers in range(15,1,-1):
  for num in vals[numPapers]: #one individual combination, like (0,0,2,1,2)
    num_sheets = sum(num)
    for choice in range(len(num)): #which size we're grabbing 1,2,4,etc
      
      if num[choice] <= 0: #if we don't have any papers of size X, skip it.
        continue
      
      
      new_item = list(num) #decrement the # of papers of size X
      new_item[choice] -= 1
      #by using size X, we make one new paper of size X/2, X/4, etc
      for spot in range(choice+1,len(num)): 
        new_item[spot] +=1
      
      
      #increment the counter for the paper combinations, if in dictionary already, increment, else just put into there.
      
      #vals[numPapers][num] = percent chance of getting a certain paper distribution to begin with like (0,1,3,2)
      #num[choice]*1.0/num_sheets = if we have 3 pages of size 2, we have 3/(total number of sheets) chance of drawing a page of size 2
      if tuple(new_item) in vals[numPapers-1]:
        vals[numPapers-1][tuple(new_item)] += vals[numPapers][num]*num[choice]*1.0/num_sheets
      else:
        vals[numPapers-1][tuple(new_item)] = vals[numPapers][num]*num[choice]*1.0/num_sheets
      
        
        
  print numPapers-1, len(vals[numPapers-1])

#we want percent at 8, 4, and 2
print round(vals[8][(0,1,0,0,0)] + vals[4][(0,0,1,0,0)]+vals[2][(0,0,0,1,0)],6)
print "Time Taken:", time.time() - start


"""
0.464399
Time Taken: 0.0016040802002

Well, I detailed the code above so hopefully the comments help me if I have to go back to this.



"""
