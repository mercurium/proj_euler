import time
start = time.time()

def c(a):
    yield ''.join(a[1:]) + '0'
    yield ''.join(a[1:]) + '1'

n = 5
tot = 0
stack = [('0'*n, frozenset(['0'*n]), ['0b'])]
while stack:
    a, v, i = stack.pop()
    if len(v) == 2 ** n:
        tot += int(''.join(i),2) // (2 ** (n - 1))
    else:
        for x in c(a):
            if x not in v:
                stack += [(x, v | frozenset([x]), i + [x[-1]])]

print(tot)
print "Time Taken:", time.time() -start

