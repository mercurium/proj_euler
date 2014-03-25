import string, time
START = time.time()

fileRead = open('roman.txt','r')
romanNumbers = string.split(fileRead.read().strip(),'\n')
roman = [('M',1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L',50), ('XL', 40), ('X',10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

def romanToDec(Str):
    sumz = 0
    charPtr = 0
    strPtr = 0
    while strPtr < len(Str) and charPtr < len(roman):
        currentLetter, currentVal = roman[charPtr]
        if currentLetter == Str[strPtr:strPtr+len(currentLetter)]:
            sumz += currentVal
            strPtr += len(currentLetter)
        else:
            charPtr += 1
    return sumz

def decToRoman(val):
    strz = ""
    charPtr = 0
    while val > 0:
        currentLetter, currentVal = roman[charPtr]
        if currentVal <= val:
            strz += currentLetter
            val -= currentVal
        else:
            charPtr += 1
    return strz
    
charCountSaved = 0
for romanNum in romanNumbers:
    saved = len(romanNum) - len( decToRoman( romanToDec( romanNum ) ))
    charCountSaved += saved

print "The answer is:", charCountSaved
print "Time Taken:", time.time() - START
