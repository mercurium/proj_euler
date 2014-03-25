#NOTE have not cleaned up this file yet... T_T

import string
import time
START = time.time()

order = '23456789TJQKA'

def getOrder(charz):
    return string.find(order, charz)

def sort(hand): #dumb bubble sort, but the hand only has 5 cards so who cares lol.
    for i in xrange(0,len(hand)):
        for j in xrange(i, len(hand)):
            val1 = getOrder(hand[i][0])
            val2 = getOrder(hand[j][0])
            if val1 > val2:
                hand[i],hand[j] = hand[j],hand[i]
    return hand


def getCardValues(hand):
    return string.join([card[0] for card in hand])

def flush(hand): #val of highest card
    if len(  set( [card[1] for card in hand] )  ) == 1:
        return True, hand[4]
    return False, 0

def straight(hand): #val of highest card
    cardValues = getCardValues(hand)
    if cardValues not in order:
        return False, 0
    return True, hand[4]

def fourOK(hand): #val of 4 of a kind
    cardValues = getCardValues(hand)
    if cardValues[0]== cardValues[3] or cardValues[1] == cardValues[4]:
        return True, hand[2]
    return False, 0
    
def threeOK(hand): #val of 3 of a kind
    cardValues = getCardValues(hand)
    if cardValues[0]== cardValues[2] or cardValues[1] == cardValues[3] \
      or cardValues[2] == cardValues[4]:
        return True, hand[2]
    return False, 0

def twoOK(hand): #val of 2 of a kind
    cardVals = getCardValues(hand)
    if threeOK(hand)[0]:
        if cardVals[0] == cardVals[1] and cardVals[3]==cardVals[4]:
            if cardVals[1] == cardVals[2]:
                return True, cardVals[3]
            return True, cardVals[1]
        return False, 0
    if cardVals[0]==cardVals[1] or cardVals[1]==cardVals[2]:
        return True, cardVals[1]+cardVals[4]
    if cardVals[2] == cardVals[3]:
        return True, cardVals[3]+cardVals[4]
    if cardVals[3] == cardVals[4]:
        return True, cardVals[3]+cardVals[2]
    return False, 0

def twoP(hand):
    cardVals = getCardValues(hand)
    if cardVals[0] == cardVals[1] and cardVals[2]==cardVals[3]:
        return True, hand[0], hand[2]
    elif cardVals[0] == cardVals[1] and cardVals[3]==cardVals[4]:
        return True, hand[0], hand[3]
    elif cardVals[1] == cardVals[2] and cardVals[3]==cardVals[4]:
        return True, hand[1], hand[3]
    return False, 0

def max(hand):
    hand = sort(hand)
    f = flush(hand)
    s = straight(hand)
    four = fourOK(hand)
    three = threeOK(hand)
    two = twoOK(hand)
    tP = twoP(hand)
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
        return 2, hand[4] #single, returns highest card


fileRead = open('poker.txt', 'r')
hands = string.split(fileRead.read().strip(),'\n')
hands = [string.split(hand," ") for hand in hands]

wins = 0
losses = 0
i = 0
for hand in hands:
    hand1 = sort(hand[:5])
    hand2 = sort(hand[5:])
    val1 = max(hand1)
    val2 = max(hand2)
    print val1,val2
    if val1[0] > val2[0]: #check who has the higher type of hand 
        wins = wins + 1
    elif val1[0] < val2[0]:
        losses = losses + 1
    elif getOrder(val1[1][0]) > getOrder(val2[1][0]): #equivalent hand type, check number
        wins = wins + 1
    elif getOrder(val1[1][0]) < getOrder(val2[1][0]):
        losses =losses +1

    elif getOrder(val1[1][1]) > getOrder(val2[1][1]):
        wins = wins + 1
    elif getOrder(val1[1][1]) < getOrder(val2[1][1]):
        losses =losses +1

print wins, losses
print "Time Taken:", time.time() - START
    
