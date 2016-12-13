#NOTE TODO need to solve it
import time
from itertools import product
START = time.time()
BASE  = 33


def kaprekarRoutine(lst, base):
  b = sorted(lst)
  a = b[::-1]
  if a[0] == b[0]:
    return lst
  for j in range(len(a)-1,-1,-1):
    a[j] -= b[j]
    if a[j] < 0:
      a[j]   += base
      a[j-1] -= 1
  return tuple(a)

resultCache = dict()
def getCount(tup, base):
  if (tup,base) in resultCache:
    return resultCache[(tup, base)]

  kaprekard = kaprekarRoutine(tup, base)
  if kaprekard == tup:
    return 0
  resultCache[(tup, base)] = getCount(kaprekard, base) + 1
  return resultCache[(tup, base)]

countLst = [0]*40
for tup in product(range(BASE), repeat=5):
  countLst[getCount(tup,BASE)] += 1

countLst = filter(lambda x: x, countLst)

print countLst, sum([x * y for x,y in enumerate(countLst)])
print len(countLst)

print "Time Taken:", time.time() - START

"""

BASE = 15
[16, 14899, 27650, 58090, 106850, 102340, 55660, 44670, 41240, 87240, 129560, 63560, 24490, 3110] 5274369
Time Taken: 1.38765501976
14
>>>>

15-1, 15000-101,30000-2000-300-50,

BASE = 21
[22, 41019, 70230, 105550, 214240, 297260, 418420, 396430, 326810, 549070, 563150, 527580, 358840, 157770, 51450, 6260] 34289199
Time Taken: 8.19531702995
>>>> len(countLst)
16
>>>>

BASE = 27
[28, 87299, 139690, 219730, 520400, 1071040, 1399100, 1204590, 1282210, 1256830, 1378760, 1732030, 1627990, 1210470, 758260, 339530, 104670, 16020, 260] 132630799
19
Time Taken: 30.5993869305
>>>>
BASE = 33
[34, 159499, 241790, 392470, 928480, 1584650, 2177800, 3262860, 3882160, 3301490, 3711930, 4495710, 3846360, 3489940, 3139520, 2283690, 1395230, 629960, 195700, 16120] 403303329
20
Time Taken: 95.1963000298


"""
