import time
START = time.time()

SIZE = 50000

lfg = []
for k in xrange(1,56):
    lfg.append( (100003 - 200003 * k + 300007 * k**3) % (10**6) )
for k in xrange(56,SIZE*6+1):
    lfg.append( (lfg[-24] + lfg[-55]) % (10**6))

for k in xrange(0,len(lfg),6):
    for i in xrange(0,3): lfg[k+i] = lfg[k+i] %10000
    for i in xrange(3,6): lfg[k+i] = lfg[k+i] % 399 +1

print lfg[:12], len(lfg)

lfg = [lfg[6*k:6*k+6] for k in range(0,SIZE)]
lfg.sort()

print len(lfg)

volume = 0
for c in lfg:
    volume += c[3] * c[4] * c[5]
for i in xrange(SIZE):
    break
    a = lfg[i]
    for j in xrange(i+1,SIZE):
        b = lfg[j]
        if b[0] > a[0] + a[3]:
            break
        if a[1] <= b[1] < a[1] + a[4] and a[2] <= b[2] < a[2] + a[5]:
            volume -= min(a[0] +a[3] - b[0], b[3]) * \
                     min(a[1] +a[4] - b[1], b[4]) * \
                     min(a[2] +a[5] - b[2], b[5])
        elif a[1] <= b[1] < a[1] + a[4] and b[2] <= a[2] < b[2] + b[5]:
            volume -= min(a[0] +a[3] - b[0], b[3]) * \
                     min(a[1] +a[4] - b[1], b[4]) * \
                     min(b[2] +b[5] - a[2], a[5])
        elif b[1] <= a[1] < b[1] + b[4] and a[2] <= b[2] < a[2] + a[5]:
            volume -= min(a[0] +a[3] - b[0], b[3]) * \
                     min(b[1] +b[4] - a[1], a[4]) * \
                     min(a[2] +a[5] - b[2], b[5])
        elif b[1] <= a[1] < b[1] + b[4] and b[2] <= a[2] < b[2] + b[5]:
            volume -= min(a[0] +a[3] - b[0], b[3]) * \
                     min(b[1] +b[4] - a[1], a[4]) * \
                     min(b[2] +b[5] - a[2], a[5])
    #print i


print volume

print "Time Taken:", time.time() - START
