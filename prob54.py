import string
import time
start = time.time()




order = '23456789TJQKA'
true, false = 1,0

def od(charz):
  return string.find(order, charz)

def sort(lst):
  lenz = len(lst)
  for i in range(0,lenz):
    for j in range(i, lenz):
      val1 = od(lst[i][0])
      val2 = od(lst[j][0])
      if val1 > val2:
        lst[i],lst[j] = lst[j],lst[i]
  return lst


def gf(lst):
  return lst[0][0]+lst[1][0]+lst[2][0]+lst[3][0]+lst[4][0]

def flush(lst): #val of highest card
  suit = lst[0][1]
  if suit == lst[1][1] and suit == lst[2][1] and suit == lst[3][1] and suit == lst[4][1]:
    return true, lst[4]
  return false, 0

def straight(lst): #val of highest card
  item = gf(lst)
  if string.find(order, item) == -1:
    return false, 0
  return true, item[4]

def fourOK(lst): #val of 4 of a kind
  item = gf(lst)
  if item[0]== item[3] or item[1] == item[4]:
    return true, item[2]
  return false, 0
  
def threeOK(lst): #val of 3 of a kind
  i = gf(lst)
  if i[0]== i[2] or i[1] == i[3] or i[2] == i[4]:
    return true, i[2]
  return false, 0

def twoOK(lst): #val of 2 of a kind
  i = gf(lst)
  if threeOK(lst)[0]:
    if i[0] == i[1] and i[3]==i[4]:
      if i[1] == i[2]:
        return true, i[3]
      return true, i[1]
    return false, 0
  if i[0]==i[1] or i[1]==i[2]:
    return true, i[1]+i[4]
  if i[2] == i[3]:
    return true, i[3]+i[4]
  if i[3] == i[4]:
    return true, i[3]+i[2]
  return false, 0

def twoP(lst):
  i = gf(lst)
  if i[0] == i[1] and i[2]==i[3]:
    return true, i[0], i[2]
  elif i[0] == i[1] and i[3]==i[4]:
    return true, i[0], i[3]
  elif i[1] == i[2] and i[3]==i[4]:
    return true, i[1], i[3]
  return false, 0

def max(lst):
  lst = sort(lst)
  f = flush(lst)
  s = straight(lst)
  four = fourOK(lst)
  three = threeOK(lst)
  two = twoOK(lst)
  tP = twoP(lst)
  if f[0] and s[0]:
    return 10, s[1] #straight flush, return high card
  elif four[0]:
    return 9, four[1] #4 of a kind, return number
  elif three[0] and two[0]:
    return 8, three[1] #full house, return triple
  elif f[0]:
    return 7, f[1] #flush, return high card
  elif s[0]:
    return 6, s[1] #straight, return high card
  elif three[0]:
    return 5, three[1] #3 of a kind, return high card
  elif tP[0]:
    return 4, tP[2]+tP[1] #2 pair, return 2 pair nums
  elif two[0]:
    return 3, two[1] #pair, returns pair type
  else:
    return 2, lst[4] #single, returns highest card


temp = open('poker.txt', 'r')
lst = string.split(temp.read(),'\n')[:-1]

for i in range(0, len(lst)):
  lst[i] = string.split(lst[i],' ')

wins = 0
losses = 0
i = 0
for item in lst:
  if i >= 1000:
    break
  hand1 = sort(item[:5])
  hand2 = sort(item[5:])
  val1 = max(hand1)
  val2 = max(hand2)
  #print hand1, hand2
  #print val1, val2
  if val1[0] > val2[0]:
    wins = wins + 1
  elif val1[0] < val2[0]:
    losses = losses + 1
  elif od(val1[1][0]) > od(val2[1][0]):
    wins = wins + 1
  elif od(val1[1][0]) < od(val2[1][0]):
    losses =losses +1
  else:
    if od(val1[1][1]) > od(val2[1][1]):
      wins = wins + 1
    elif od(val1[1][1]) < od(val2[1][1]):
      losses =losses +1
  i = i+1

print wins, losses
print "Time Taken: " + str(time.time()-start)
  
