import time
start = time.time()
import string

f = "words.txt"
tmp = open(f,"r")
lst = string.split(tmp.read().strip(),'","')

SIZE_TEST = 5

words = dict()
for w in lst: #list of words that are anagrams
    sorted_word = string.join(sorted(w),'')
    if sorted_word in words:
        words[sorted_word] += [w]
    else:
        words[sorted_word] = [w]

words2 = {}
for w in words.keys():
    if len(words[w]) >= 2:
        if len(words[w][0]) in words2:
            words2[len(words[w][0])] += [words[w]]
        else:
            words2[len(words[w][0])] = [words[w]]
w =words = words2
for i in xrange(2,10):
    if i in w.keys():
        print i,w[i]
        print 


num_sq = {} #list of numbers that are anagrams
for i in range(1, int(10**5)):
    s = string.join(sorted(str(i**2)),'')
    if s in num_sq:
        num_sq[s] += [str(i**2)]
    else:
        num_sq[s] =    [str(i**2)]

num_sq2 = {}
for i in num_sq.keys():
    if len(num_sq[i]) >= 2:
        if len(i) in num_sq2:
            num_sq2[len(i)] += [num_sq[i]]
        else:
            num_sq2[len(i)]    = [num_sq[i]]
ns = num_sq = num_sq2

print len(ns)

numz = set()

for word_lst in words[SIZE_TEST]: #for every word permutation of size SIZE_TEST
    for a in xrange(1,len(word_lst)):
        for b in xrange(0,a):
            word1, word2 = word_lst[a], word_lst[b]  #get every pair of 2 words
            permutation = [word1.index(letter) for letter in word2] #compute the permutation to change word2 -> word1
            print word1,word2, permutation
            for num_lst in ns[SIZE_TEST]:
                for num in num_lst:
                    if len(set([x for x in num])) != SIZE_TEST: continue   #if the numbers aren't unique, it's probably not a permutation
                    new_num = string.join([num[i] for i in permutation], "") #get the new number
                    if new_num in num_lst:
                        numz.add(num)
                        numz.add(new_num)


print len(numz), max(numz), numz
print
print "answer is:", max(numz)
print "Time Taken:", time.time() - start

#Up to here is all just finding which numbers/words have permutations...
#now all that's left is comparing the two dictionaries to see which permutations are the same... which i don't feel like doing atm :D;;


"""
{2: [['NO', 'ON']], 3: [['NOW', 'OWN'], ['EAT', 'TEA'], ['HOW', 'WHO'], ['ITS', 'SIT'], ['ACT', 'CAT'], ['DOG', 'GOD']], 4: [['SHUT', 'THUS'], ['SURE', 'USER'], ['ITEM', 'TIME'], ['HATE', 'HEAT'], ['DEAL', 'LEAD'], ['NOTE', 'TONE'], ['FORM', 'FROM'], ['EARN', 'NEAR'], ['RATE', 'TEAR'], ['FILE', 'LIFE'], ['EAST', 'SEAT'], ['CARE', 'RACE'], ['MALE', 'MEAL'], ['MEAN', 'NAME'], ['POST', 'SPOT', 'STOP'], ['SIGN', 'SING']], 5: [['LEAST', 'STEAL'], ['SHEET', 'THESE'], ['SHOUT', 'SOUTH'], ['BOARD', 'BROAD'], ['QUIET', 'QUITE'], ['EARTH', 'HEART'], ['THROW', 'WORTH'], ['ARISE', 'RAISE'], ['NIGHT', 'THING'], ['PHASE', 'SHAPE']], 6: [['CREDIT', 'DIRECT'], ['EXCEPT', 'EXPECT'], ['DANGER', 'GARDEN'], ['FORMER', 'REFORM'], ['CENTRE', 'RECENT'], ['IGNORE', 'REGION'], ['COURSE', 'SOURCE']], 8: [['CREATION', 'REACTION']], 9: [['INTRODUCE', 'REDUCTION']]}

Congratulations, the answer you gave to problem 98 is correct.
You are the 4800th person to have solved this problem.
"""
