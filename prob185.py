#NOTE TODO need to solve it
import time
START = time.time()

data = open('data185.txt','r')
data = data.read()

guesses = [[int(x) for x in g] for g in data.split()[::2]]
correct = [int(x) for x in data.split()[1::2] ]
count = [0]

c = [set() for x in range(16)]
for g in guesses:
    for i in range(16):
        c[i].add(g[i])
print [len(x) for x in c]


a = [-1] * 16
def base_case():
    count[0] +=1
    num_correct = correct[:]
    for g in xrange(len(guesses)):
        for i in xrange(len(a)):
            if guesses[g][i] == a[i]:
                num_correct[g] -=1
                if num_correct[g] < 0:
                    return False
    if min(num_correct) == max(num_correct) == 0:
        print a
        return True
    return False


def recurse(level):
    count[0] +=1
    if count[0] % 1024 == 0:
        print count[0], a
    while level != 14 and a[level] != -1:
        level +=1
    for g in xrange(len(guesses)):
        num_correct = correct[g]
        for i in xrange(level):
            if guesses[g][i] == a[i]:
                num_correct -=1
                if num_correct < 0:
                    return False
        if (16-level) < num_correct:
            return False
    for a[level] in xrange(10):
        if level != 15:
            if recurse(level+1):
                return True
        else:
            if base_case():
                return True
    a[level] = -1
    return False


for a[0] in xrange(0,10):
    continue
    recurse(1)

print "Time Taken:", time.time()-START
    
