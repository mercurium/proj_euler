import string
import time

start = time.time()
#I, II, III, IV, V, VI, VII, IIX, IX
#I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
ones = [0,1,2,3,2,1,2,3,4,2]
temp = open('roman.txt','r')
lst = string.split(temp.read(),'\n')[:-1]
roman = {'I':1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M':1000}


def roman_to_dec(strz):
  sumz2=0
  for i in range(0, len(strz) -1):
    if roman[strz[i]] >= roman[strz[i+1]]:
      sumz2 += roman[strz[i]]
    else: sumz2 -= roman[strz[i]]
  sumz2 += roman[strz[-1]]
  return sumz2

def min_calc(intz):
  sumz2 = 0
  if intz > 1000:
    sumz2 += intz//1000
    intz = intz %1000
  item = str(intz)

  for letter in item:
    sumz2 += ones[int(letter)]
  return sumz2

sumz = 0
for i in range(0,len(lst)):
  item = lst[i]
  sumz = sumz +  len(item) - min_calc(roman_to_dec(item))

  
print sumz
print "Time Taken: " + str(time.time() - start)
