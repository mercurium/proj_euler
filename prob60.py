import time
start = time.time()
from primes import *

ps = [str(i) for i in ([3]+primes[3:2000])]#29]) ] #ps for primes_small
vals = {} #vals = dict of primes that can concatenate to primes
pset = set(ps)


for i in xrange(0,len(ps)):
	wv = set() #wv for values that work, working values
	for j in xrange(0,len(ps)):
		if m_r(int(ps[i] + ps[j])) and m_r(int(ps[j] + ps[i])):
			wv.add(ps[j])
	vals[ps[i]] = wv
print vals['13']
print "Time Taken:", time.time() - start	

def main():
	for i in ps:
		pset2 = pset.intersection(vals[i]) 
		if len(pset2) == 0: continue
		for j in ps:
			if j not in pset2: continue
			pset3 = pset2.intersection(vals[j])
			if len(pset3) == 0: continue
			for k in ps:
				if k not in pset3: continue
				pset4 = pset3.intersection(vals[k])
				if len(pset4) == 0: continue
				for a in ps:
					if a not in pset4: continue
					pset5 = pset4.intersection(vals[a])
					if len(pset5) == 0: continue
					else:
						print len(pset2),len(pset3),len(pset4),len(pset5)
						return i,j,k,a,list(pset5)[0]
				
print main()
print "Time Taken:", time.time() - start 

#Time Taken: 36.2037830353
#Time Taken: 18.6851558685 (on desktop)
#13 5197 5701 6733 8389
#93 5 2 1 this was the size of the list

