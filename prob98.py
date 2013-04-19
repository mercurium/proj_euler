import time
start = time.time()
import string

f = "words.txt"
tmp = open(f,"r")
lst = string.split(tmp.read().strip(),'","')

words = dict()
for w in lst: #list of words that are anagrams
  sorted_word = string.join(sorted(w),'')
  try:
    words[sorted_word] += [w]
  except:
    words[sorted_word] = [w]

words2 = {}
for w in words.keys():
  if len(words[w]) >= 2:
    try:
      words2[len(words[w][0])] += [words[w]]
    except:
      words2[len(words[w][0])] = [words[w]]
w =words = words2
print words2

num_sq = {} #list of numbers that are anagrams
for i in range(1, int(10**4.5)):
  s = string.join(sorted(str(i**2)),'')
  try:
    num_sq[s] += [str(i**2)]
  except:
    num_sq[s] =  [str(i**2)]

num_sq2 = {}
for i in num_sq.keys():
  if len(num_sq[i]) >= 2:
    try:
      num_sq2[len(i)] += [num_sq[i]]
    except:
      num_sq2[len(i)]  = [num_sq[i]]
ns = num_sq = num_sq2

print len(num_sq2)


print "Time Taken:", time.time() - start


#now all that's left is comparing the two dictionaries to see which permutations are the same... which i don't feel like doing atm :D;;


"""
{2: [['NO', 'ON']], 3: [['NOW', 'OWN'], ['EAT', 'TEA'], ['HOW', 'WHO'], ['ITS', 'SIT'], ['ACT', 'CAT'], ['DOG', 'GOD']], 4: [['SHUT', 'THUS'], ['SURE', 'USER'], ['ITEM', 'TIME'], ['HATE', 'HEAT'], ['DEAL', 'LEAD'], ['NOTE', 'TONE'], ['FORM', 'FROM'], ['EARN', 'NEAR'], ['RATE', 'TEAR'], ['FILE', 'LIFE'], ['EAST', 'SEAT'], ['CARE', 'RACE'], ['MALE', 'MEAL'], ['MEAN', 'NAME'], ['POST', 'SPOT', 'STOP'], ['SIGN', 'SING']], 5: [['LEAST', 'STEAL'], ['SHEET', 'THESE'], ['SHOUT', 'SOUTH'], ['BOARD', 'BROAD'], ['QUIET', 'QUITE'], ['EARTH', 'HEART'], ['THROW', 'WORTH'], ['ARISE', 'RAISE'], ['NIGHT', 'THING'], ['PHASE', 'SHAPE']], 6: [['CREDIT', 'DIRECT'], ['EXCEPT', 'EXPECT'], ['DANGER', 'GARDEN'], ['FORMER', 'REFORM'], ['CENTRE', 'RECENT'], ['IGNORE', 'REGION'], ['COURSE', 'SOURCE']], 8: [['CREATION', 'REACTION']], 9: [['INTRODUCE', 'REDUCTION']]}
"""
