import time, string
from sympy import *
from math import factorial as fa


START       = time.time()
MAX_LETTERS = 15
wordStr     = "thereisasyetinsufficientdataforameaningfulanswer"

def addToDict(valDict, key, val, func=(lambda x,y: x+y)):
  if key not in valDict:
    valDict[key] = val
  else:
    valDict[key] = func(valDict[key], val)

def countAllLenPerm(wordDict, maxLen):
  counts   = [0] * (max(wordDict.values())+1)
  x        = symbols('x')
  multiple = 1
  val      = 1

  for value in wordDict.values():
    counts[value] += 1

  for i in xrange(1,len(counts)):
    val      += x**i / fa(i)
    multiple *= val**counts[i]

  coeff = Poly(expand(multiple)).all_coeffs()[::-1]
  return sum(coeff[x] * fa(x) for x in xrange(0,maxLen+1))

def wordToNum(word, letterCount):
  count   = 0
  lcClone = letterCount.copy()

  for letterSame in xrange(len(word)):
    precedingLetters = set(filter( \
          (lambda x: ord(x) < ord(word[letterSame]) \
            and lcClone[x] != 0), \
          lcClone.keys()) \
        )

    for leadDiffLetter in precedingLetters:
      lcClone[leadDiffLetter] -= 1
      count += countAllLenPerm(lcClone, MAX_LETTERS - letterSame -1)
      lcClone[leadDiffLetter] += 1

    lcClone[word[letterSame]] -= 1

  return count + len(word)

def numToWord(number, letterCount):
  count   = 0
  lcClone = letterCount.copy()
  word    = ""

  for numLettersFixed in xrange(MAX_LETTERS):
    letters = sorted(filter((lambda x: lcClone[x] != 0), letterCount.keys()))
    for leadDiffLetter in letters:

      lcClone[leadDiffLetter] -= 1
      thisLetterCount = countAllLenPerm(lcClone, MAX_LETTERS - numLettersFixed -1)
      lcClone[leadDiffLetter] += 1

      if thisLetterCount + count < number:
        count += thisLetterCount
      else:
        count                   += 1
        lcClone[leadDiffLetter] -= 1
        word                    += leadDiffLetter
        break
    if count == number:
      break
  return word

letterCount = dict()
for letter in wordStr:
  addToDict(letterCount, letter, 1)

P = lambda x: wordToNum(x, letterCount)

number = P("legionary") + P("calorimeters") - P("annihilate") + P("orchestrated") - P("fluttering")

print numToWord(number, letterCount)
print "Time Taken:", time.time() - START


"""

jchen@jchen-mbp 22:12:41 ~/Developer/proj_euler(master|✚2…) % pypy -i prob480.py
turnthestarson
451023621685297214
Time Taken: 18.4942340851
Time Taken: 14.4409170151


Congratulations, the answer you gave to problem 480 is correct.
You are the 351st person to have solved this problem.


"""
