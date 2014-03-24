import time
START = time.time()
item_pows = set()
for a in xrange(2,101): #meh lol, only 10**4 items. Not worth optimizing... xD. Letting Python's hashing take care of duplicates for me.
	for b in xrange(2,101):
		item_pows.add(a**b)
print len(item_pows)
print "Time Taken:", time.time() - START
